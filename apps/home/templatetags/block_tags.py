from django import template

register = template.Library()


@register.simple_tag()
def get_identifier(item):
    return id(item)


@register.simple_tag()
def get_video_provider(url):
    if 'youtube' in url:
        return 'YouTube', 'https://www.google.de/intl/de/policies/privacy/'
    return 'Vimeo', 'https://vimeo.com/privacy'
