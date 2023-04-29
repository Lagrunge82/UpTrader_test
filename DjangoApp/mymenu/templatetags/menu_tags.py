from django import template
from mymenu.utils import MenuBuilder

register = template.Library()


@register.tag(name='draw_menu')
def do_draw_menu(parser, token):
    try:
        tag_name, menu = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(f"{tag_name} tag requires exactly one argument")
    return MenuBuilder(menu)
