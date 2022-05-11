import sib_api_v3_sdk
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import ListView
from sib_api_v3_sdk.rest import ApiException
from wagtail.core.models import Page
from wagtail.search.backends import get_search_backend

from apps.contrib.forms import NewsletterForm
from apps.contrib.translations import get_search_fields


class SearchResultsView(ListView):
    template_name = 'search_results.html'

    def get_queryset(self):
        sb = get_search_backend()
        query = self.request.GET.get('q')
        res = sb.search(query, Page, fields=get_search_fields())
        return res


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)

        if form.is_valid():
            configuration = sib_api_v3_sdk.Configuration()
            configuration.api_key['api-key'] = settings.SENDINBLUE_API_KEY
            api_instance = sib_api_v3_sdk.ContactsApi(
                sib_api_v3_sdk.ApiClient(configuration))
            create_doi_contact = sib_api_v3_sdk.CreateDoiContact(
                email=form.cleaned_data['email'], include_list_ids=[2],
                template_id=2, redirection_url='https://liqd.net')
            try:
                api_instance.create_doi_contact(create_doi_contact)
                return HttpResponse(status=204)
            except ApiException as e:
                print(
                    "Exception when calling ContactsApi->create_doi_contact: "
                    "%s\n" % e)
        return JsonResponse(form.errors, status=400)
