from django.conf import settings
from django.views.generic import ListView
from wagtail.core.models import Page
from wagtail.search.backends import get_search_backend

from apps.contrib.translations import get_search_fields


class CustomQueryCompiler:
    queryset = Page.objects.all()


class SearchResultsView(ListView):
    template_name = 'search_results.html'

    def get_queryset(self):
        sb = get_search_backend()
        sb.query_compiler = CustomQueryCompiler()
        # needs to be set otherwise _get_results_from_hits will fail
        sb._score_field = False
        query = self.request.GET.get('q')
        res = sb.es.search(index=settings.WAGTAILSEARCH_BACKENDS["default"]
                           ["INDEX"] + "__wagtailcore_page",
                           _source=False,
                           size=100, stored_fields="pk",
                           query={"multi_match":
                                  {"query": query,
                                   "fields": get_search_fields(),
                                   "type": "best_fields",
                                   "operator": "OR",
                                   "slop": 0,
                                   "prefix_length": 0,
                                   "max_expansions": 50,
                                   "zero_terms_query": "NONE",
                                   "auto_generate_synonyms_" +
                                   "phrase_query": True,
                                   "boost": 1.0}})
        res = sb.results_class._get_results_from_hits(sb, res['hits']['hits'])
        return res
