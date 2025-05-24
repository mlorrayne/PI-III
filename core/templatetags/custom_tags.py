from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='add_attr')
def add_attr(field, attr):
    if hasattr(field, 'as_widget'):
        attrs = {}
        key, val = attr.split('=')
        attrs[key] = val
        return field.as_widget(attrs=attrs)
    return mark_safe(str(field))
