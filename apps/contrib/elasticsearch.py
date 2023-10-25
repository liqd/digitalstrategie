from wagtail.search.backends.elasticsearch7 import \
    Elasticsearch7AutocompleteQueryCompiler
from wagtail.search.backends.elasticsearch7 import Elasticsearch7SearchBackend
from wagtail.search.backends.elasticsearch7 import Elasticsearch7SearchResults


# Code below taken and modified from wagtails elasticsearch backend
class ElasticsearchCustomQueryCompiler(
    Elasticsearch7AutocompleteQueryCompiler
):
    # we override this to remove the check if the field exists on the model
    # as we use a glob pattern (e.g. *page_title_en)
    def check(self):
        self._get_filters_from_where_node(self.queryset.query.where,
                                          check_only=True)
        list(self._get_order_by())


class ElasticsearchResults(Elasticsearch7SearchResults):
    def _get_es_body(self, for_count=False):
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
        pks = [hit['fields']['pk'][0] for hit in hits]
        scores = {str(hit['fields']['pk'][0]): hit['_score'] for hit in hits}
        highlights = {}

        results = {str(pk): None for pk in pks}
        for hit in hits:
            hs = hit['highlight']
            hs.pop('content_type')
            for highlight in hs.values():
                # we only need one highlight
                if hit['fields']['pk'][0] not in highlights:
                    highlights[str(hit['fields']['pk'][0])] = highlight[0]
                    break

        for obj in self.query_compiler.queryset.filter(pk__in=pks):
            results[str(obj.pk)] = obj

            if self._score_field:
                setattr(obj, self._score_field, scores.get(str(obj.pk)))
            setattr(obj, 'highlight', highlights.get(str(obj.pk)))
        for pk in pks:
            result = results[str(pk)]
            if result:
                yield result


class ElasticsearchCustomSearchBackend(Elasticsearch7SearchBackend):
    results_class = ElasticsearchResults
    autocomplete_query_compiler_class = ElasticsearchCustomQueryCompiler


SearchBackend = ElasticsearchCustomSearchBackend
