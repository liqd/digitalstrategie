import os

from django import template
from django.conf import settings
from django.core import management
from django.core.cache import cache
from django.core.paginator import Paginator
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


@register.simple_tag
def combined_url_parameter(request_query_dict, **kwargs):
    combined_query_dict = request_query_dict.copy()
    for key in kwargs:
        combined_query_dict.setlist(key, [kwargs[key]])
    encoded_parameter = "?" + combined_query_dict.urlencode()
    return encoded_parameter


@register.simple_tag
def get_proper_elided_page_range(p, number, on_each_side=1, on_ends=1):
    paginator = Paginator(p.object_list, p.per_page)
    return paginator.get_elided_page_range(
        number=number, on_each_side=on_each_side, on_ends=on_ends
    )


@register.simple_tag
def get_has_translation(page, lang_code):
    """Return true if there is content in the specified language.

    There is content, if any of the translated fields has content. Relies on
    naming the panels of the language tab {lang_code}_content_panels.
    """
    if hasattr(page, '{}_content_panels'.format(lang_code)):
        content_panels = getattr(page, '{}_content_panels'.format(lang_code))
        for panel in content_panels:
            field_name = panel.field_name
            if getattr(page, field_name):
                return True
    return False
