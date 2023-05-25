from django import template
from wagtail.models import Site
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
    if request is None:
        return ""
    if not model:
        model = context.get('self', None)
        root = Site.find_for_request(request).root_page.specific
        while not hasattr(model, 'get_meta_title') or (
                not model.get_meta_title() and
                not model.get_meta_description()):
            if model == root:
                return tags.meta_tags(request, model)
            model = model.specific.get_parent().specific

    return tags.meta_tags(request, model)
