# -*- coding: utf-8 *-*
from django import template
import feedparser
import datetime
register = template.Library()

@register.inclusion_tag('blog.html')
def pull_feed(feed_url, posts_to_show=1):
	feed = feedparser.parse(feed_url)
	posts = []
	for i in range(posts_to_show):
		posts.append({
			'title': feed['entries'][i].title,
			'summary': feed['entries'][i].summary,
			'link': feed['entries'][i].link,
			})
	return {'posts': posts}
