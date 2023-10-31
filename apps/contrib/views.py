from django.views.generic import ListView
from wagtail.models import Page
from wagtail.search.backends import get_search_backend

from apps.contrib.translations import get_search_fields


class SearchResultsView(ListView):
    template_name = 'search_results.html'

    def get_queryset(self):
        sb = get_search_backend()
        query = self.request.GET.get('q', '')
        res = sb.autocomplete(query, Page, fields=get_search_fields())
        return res
