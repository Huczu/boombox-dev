import re
from django import template

register = template.Library()


@register.filter(name='youtube_id')
def yt_id(value):
    """Gets youtube id"""
    regex = re.compile("v=(?P<id>\w+)")
    r = regex.search(value)
    try:
        return r.groups()[0]
    except AttributeError, e:
        print(e)
        return ""


@register.filter(name='vimeo_id')
def vi_id(value):
    """Gets vimeo id from url"""
    regex = re.compile("http://vimeo.com/(?P<id>\d+)")
    r = regex.search(value)
    try:
        return r.groups()[0]
    except AttributeError, e:
        print(e)
        return ""
