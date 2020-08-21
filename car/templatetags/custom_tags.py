from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='split_by_comma')
@stringfilter
def split_by_comma(value):
    return  value.split(',')


@register.filter(name='increase_price')
def increase_price(value, arg):
    try:
        arg = float(arg)
    except:
        arg = 2
    return  int(value * arg)
