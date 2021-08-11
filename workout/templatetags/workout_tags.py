from django import template

register = template.Library()

@register.filter
def convert_to_minutes(value):
    seconds = float(value)-int(value)
    return '{}:{:02d}'.format(int(value),int(seconds*60))

@register.filter
def two_d_int(value):
    return '{:02d}'.format(value)