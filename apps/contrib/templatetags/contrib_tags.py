import os

from django import template
from django.conf import settings
from django.core import management
from django.core.cache import cache
from django.utils.html import mark_safe

register = template.Library()


@register.simple_tag
def get_external_footer():
    # The BO footer needs to be included here as we can't include external
    # html in the browser. Add a cron job to update the file periodically via
    # the get_footer management command.
    if hasattr(settings, 'BERLIN_FOOTER_URL') and settings.BERLIN_FOOTER_URL:
        footer = cache.get('footer')
        if footer:
            return footer
        filepath = settings.MEDIA_ROOT + "/landesfooter.inc"
        if not os.path.isfile(filepath):
            has_error = management.call_command('get_footer')
            if has_error:
                return ''
        with open(filepath, "r") as f:
            footer = mark_safe(f.read())
            cache.set('footer', footer)
            return footer
    return ''
