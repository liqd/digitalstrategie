from django import template

from apps.snippets.models import NavigationMenu

register = template.Library()


@register.simple_tag(takes_context=False)
def load_site_menu(menu_name):
    menu = NavigationMenu.objects.filter(menu_name=menu_name)

    if menu:
        return menu[0].menu_items.all()
    else:
        return None
