import re
from django import template

register = template.Library()

def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

@register.filter(name='youtube_id')
def yt_id(value):
    """Gets youtube id"""
    regex = re.compile("v=(?P<id>\w+)")
    r = regex.search(value)
    return r.groups()[0]

@register.filter(name='vimeo_id')
def vi_id(value):
    """Gets vimeo id from url"""
    regex = re.compile("http://vimeo.com/(?P<id>\d+)")
    r = regex.search(value)
    return r.groups()[0]
