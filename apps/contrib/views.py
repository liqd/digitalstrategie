from itertools import chain
from typing import Any
from typing import List

from django.views.generic import ListView
from wagtail.search.backends import get_search_backend

from apps.contrib.translations import get_search_fields
from apps.gruenbuch.models import GruenbuchDetailPage
from apps.gruenbuch.models import GruenbuchIndexPage
from apps.gruenbuch.models import GruenbuchOverviewPage
from apps.home.models import DetailPage
from apps.home.models import HomePage
from apps.home.models import MicrositeDetailPage
from apps.home.models import MicrositeOverviewPage
from apps.home.models import OverviewPage
from apps.home.models import SimplePage
from apps.measures.models import MeasuresDetailPage
from apps.measures.models import MeasuresOverviewPage


class SearchResultsView(ListView):
    template_name = 'search_results.html'

    def get_queryset(self) -> List[Any]:
        """Return list with all search results from the different pages.

        This is an inefficient workaround for
        `sb.autocomplete(query, Page, fields=get_search_fields())` not
        returning the title in the correct language as the wagtail.models.Page
        doesn't know about it. The proper way would be to subclass Page with
        the translated title field and make all custom models inherit from that
        subclass.

         Returns:
             List of all search results

        """
        sb = get_search_backend()
        query = self.request.GET.get('q', '')
        # FIXME: Should use one query over a common page model inherited by all
        # models below
        res = list(chain(
            sb.autocomplete(query, HomePage, fields=get_search_fields()),
            sb.autocomplete(query, OverviewPage, fields=get_search_fields()),
            sb.autocomplete(query, DetailPage, fields=get_search_fields()),
            sb.autocomplete(query, MicrositeOverviewPage,
                            fields=get_search_fields()),
            sb.autocomplete(query, MicrositeDetailPage,
                            fields=get_search_fields()),
            sb.autocomplete(query, SimplePage, fields=get_search_fields()),
            sb.autocomplete(query, GruenbuchOverviewPage,
                            fields=get_search_fields()),
            sb.autocomplete(query, GruenbuchDetailPage,
                            fields=get_search_fields()),
            sb.autocomplete(query, GruenbuchIndexPage,
                            fields=get_search_fields()),
            sb.autocomplete(query, MeasuresOverviewPage,
                            fields=get_search_fields()),
            sb.autocomplete(query, MeasuresDetailPage,
                            fields=get_search_fields())
        ))
        return res
