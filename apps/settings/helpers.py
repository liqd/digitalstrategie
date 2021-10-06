from django.utils.html import mark_safe
from wagtail.core.models import Site

from apps.settings.models import ImportantPages


def add_link_to_helptext(help_text, important_page_name):
    """
    expected format for helptext: 'my helptext
    with {}link text{} to some important page'
    """
    site = Site.objects.filter(
        is_default_site=True
    ).first()
    important_pages = ImportantPages.for_site(site)

    if getattr(important_pages, important_page_name) and \
       getattr(important_pages, important_page_name).live:
        url = getattr(important_pages, important_page_name).url
        help_text = help_text \
            .format('<a href="' + url + '" target="_blank">', '</a>')
        return mark_safe(help_text)

    return help_text.format('', '')
