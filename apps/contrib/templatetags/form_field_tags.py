from django import template
from django.forms import CheckboxInput
from django.forms import CheckboxSelectMultiple

register = template.Library()


@register.filter(name='is_checkbox')
def is_checkbox(field):
    return (field.field.widget.__class__.__name__
            == CheckboxInput().__class__.__name__)


@register.filter(name='is_checkbox_select_multiple')
def is_checkbox_select_multiple(field):
    return (field.field.widget.__class__.__name__
            == CheckboxSelectMultiple().__class__.__name__)
