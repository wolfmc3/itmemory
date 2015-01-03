from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag()
def css_icon(icon):
    return render_to_string("icon.html", {'iconname': icon})