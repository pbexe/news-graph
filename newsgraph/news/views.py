from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import urllib.request
from .models import Story
import feedparser

def stories():
	# Connect to the BBC RSS feed
	news = feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml?edition=uk')
	# For every story
	for story in news.entries:
		# Return the link to that story
		yield story['link']

def index(request):
	for story in stories():
		s = Story(source=story)
		s.save()
		# print("story:", story)
		# with urllib.request.urlopen(story) as response:
		# 	html = response.read()
		# 	soup = BeautifulSoup(html, "html.parser")
		# 	try:
		# 		print(soup.find("div", {"class": "story-body"}).get_text())
		# 	except:
		# 		print("No content found")
	stories_add = Story.objects.all()
	output = '<br>======================================================================<br>'.join([i.source for i in stories_add])
	print(output)
	return HttpResponse(output)