from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag()
def fa_icon(icon):
    html = '''
        <i class="fa fa-%s"></i>
    '''
    return html % icon


