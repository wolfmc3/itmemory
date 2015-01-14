from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag()
def css_icon(icon):
    return render_to_string("icon.html", {'iconname': icon})


@register.simple_tag
def active_page(request, view_name):
    from django.core.urlresolvers import resolve, Resolver404
    if not request:
        return ""
    try:
        return "active" if resolve(request.path_info).namespace == view_name else ""
    except Resolver404:
        return ""

