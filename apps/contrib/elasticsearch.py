from wagtail.search.backends.elasticsearch8 import Elasticsearch8SearchBackend
from wagtail.search.backends.elasticsearch8 import Elasticsearch8SearchResults


# Code below taken and modified from wagtails elasticsearch backend
class ElasticsearchResults(Elasticsearch8SearchResults):

    def _get_es_body(self, for_count=False):
        """Override super method to add the highlight config."""
        body = {
            'query': self.query_compiler.get_query()
        }

        if not for_count:
            sort = self.query_compiler.get_sort()

            if sort is not None:
                body['sort'] = sort

            body['highlight'] = {
                "pre_tags": ["<b>"],
                "post_tags": ["</b>"],
                "fields": {
                    "*": {"require_field_match": True}
                }
            }
        return body

    def _get_results_from_hits(self, hits):
        """Override the super method to add the highlights from elasticsearch.

        Most of the code is copied directly from the super method. Also adds
        checks to exclude pages which are draft or password-protected.
        """
        pks = []
        scores = {}
        highlights = {}

        for hit in hits:
            hs = hit['highlight']
            hs.pop('content_type')
            if '_all_text_boost_2_0' in hs:
                # ignore hits from the _all_text field as it doesn't work with
                # our translations
                hs.pop('_all_text_boost_2_0')
            for highlight in hs.values():
                # we only need one highlight
                if hit['fields']['pk'][0] not in highlights:
                    highlights[str(hit['fields']['pk'][0])] = highlight[0]
                    # only use search results which have a valid hit
                    pks.append(hit['fields']['pk'][0])
                    scores[str(hit['fields']['pk'][0])] = hit['_score']
                    break

        results = {str(pk): None for pk in pks}
        for obj in self.query_compiler.queryset.filter(pk__in=pks):
            if not obj.live or obj.get_view_restrictions().exists():
                continue
            results[str(obj.pk)] = obj

            if self._score_field:
                setattr(obj, self._score_field, scores.get(str(obj.pk)))
            setattr(obj, 'highlight', highlights.get(str(obj.pk)))
        for pk in pks:
            result = results[str(pk)]
            if result:
                yield result


class ElasticsearchCustomSearchBackend(Elasticsearch8SearchBackend):
    results_class = ElasticsearchResults


SearchBackend = ElasticsearchCustomSearchBackend
