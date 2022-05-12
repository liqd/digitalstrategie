import sib_api_v3_sdk
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from sentry_sdk import capture_exception
from sib_api_v3_sdk.rest import ApiException

from apps.forms.models import NewsletterForm
from apps.settings.models import Newsletter as NewsletterSettings


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        newsletter_settings = NewsletterSettings.for_request(request)
        if form.is_valid():
            configuration = sib_api_v3_sdk.Configuration()
            configuration.api_key['api-key'] =\
                newsletter_settings.sendinblue_api_key
            api_instance = sib_api_v3_sdk.ContactsApi(
                sib_api_v3_sdk.ApiClient(configuration))
            create_doi_contact = sib_api_v3_sdk.CreateDoiContact(
                email=form.cleaned_data['email'],
                include_list_ids=[newsletter_settings.sendinblue_list_id],
                template_id=newsletter_settings.sendinblue_template_id,
                redirection_url=newsletter_settings.redirect_url)
            try:
                api_instance.create_doi_contact(create_doi_contact)
                return HttpResponse(status=204)
            except ApiException as e:
                if settings.DEBUG:
                    print("Exception when calling "
                          "ContactsApi->create_doi_contact: %s\n" % e)
                else:
                    capture_exception(e)
        return JsonResponse(form.errors, status=400)
