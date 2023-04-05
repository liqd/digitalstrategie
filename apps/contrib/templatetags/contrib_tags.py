import requests
from django import template
from django.conf import settings
from django.utils.html import mark_safe

register = template.Library()


@register.simple_tag
def get_external_footer():
    if hasattr(settings, 'BERLIN_FOOTER_URL') and settings.BERLIN_FOOTER_URL:
        try:
            response = requests.get(settings.BERLIN_FOOTER_URL, timeout=2.0)
        except (requests.ConnectTimeout, requests.HTTPError, requests.Timeout):
            return ''
        return mark_safe(response.text)
    else:
        return ''
