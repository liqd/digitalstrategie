from django import template
from wagtail.core.models import Site
from wagtailmetadata import tags

register = template.Library()


@register.simple_tag(takes_context=True)
def custom_meta_tags(context, model=None):
    """Use metadata from homepage if not set on current page.

    Like https://github.com/neon-jungle/wagtail-metadata/blob/master/
    wagtailmetadata/templatetags/wagtailmetadata_tags.py
    but uses homepage meta tags if current site does not have own tags.
    """
    request = context.get('request', None)
    if not model:
        model = context.get('self', None)
        if not hasattr(model, 'get_meta_title') or (
                not model.seo_title and
                not model.get_meta_description()):
            site = Site.find_for_request(request)
            model = site.root_page.specific

    return tags.meta_tags(request, model)
