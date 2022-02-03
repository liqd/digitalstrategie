import requests
from django import template
from django.utils.html import mark_safe

register = template.Library()


@register.simple_tag
def get_external_footer():
    response = requests.get('https://www.berlin.de/rbmskzl/__i9/ohne/foot.inc')
    return mark_safe(response.text)
