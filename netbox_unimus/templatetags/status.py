from django import template

register = template.Library()

@register.filter
def status(value):
    device_unimus_status = False
    if device_unimus_status is True:
        return  "\u2705"
    else:
        return "\u274C"
