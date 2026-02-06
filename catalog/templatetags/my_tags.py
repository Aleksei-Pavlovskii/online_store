from django import template

register = template.Library()


@register.filter()
def my_filter(path):
    if path:
        return f'/media/{path}'
    return '#'