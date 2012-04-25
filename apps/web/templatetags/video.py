# -*- coding: utf-8 *-*
from django.template.defaultfilters import stringfilter
from django import template
import re

register = template.Library()

@register.filter
@stringfilter
def youtube(url):
    regex = re.compile(r"^(http://)?(www\.)?(youtube\.com/watch\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})")
    match = regex.match(url)
    if not match: return ""
    video_id = match.group('id')
    return """
    <object width="425" height="344">
    <param name="movie" value="http://www.youtube.com/watch/v/%s"></param>
    <param name="allowFullScreen" value="true"></param>
    <embed src="http://www.youtube.com/watch/v/%s" type="application/x-shockwave-flash" allowfullscreen="true" width="425" height="344"></embed>
    </object>
    """ % (video_id, video_id)
youtube.is_safe = True # Don't escape HTML
