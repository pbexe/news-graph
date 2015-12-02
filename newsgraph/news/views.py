from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import urllib.request
from .models import Story
import feedparser
import nltk

def stories():
	# Connect to the BBC RSS feed
	news = feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml?edition=uk')
	# For every story
	for story in news.entries:
		# Return the link to that story
		yield story['link']

def prepareForNLP(text):
	sentences = nltk.sent_tokenize(text)
	sentences = [nltk.word_tokenize(sent) for sent in sentences]
	sentences = [nltk.pos_tag(sent) for sent in sentences]
	return sentences

def keywords(text):
	sentences = prepareForNLP(text)
	for sentence in sentences:
		for word in sentence:
			if word[1] == "NNP":
				yield word[0]

def keywordsList(text):
	output = []
	sentences = prepareForNLP(text)
	for sentence in sentences:
		for word in sentence:
			if word[1] == "NNP":
				output.append(word[0])
	return output

def index(request):
	for story in stories():
		matches = Story.objects.filter(source=story)
		if len(matches) == 0:
			content = ""
			with urllib.request.urlopen(story) as response:
				html = response.read()
				soup = BeautifulSoup(html, "html.parser")
				try:
					content = soup.find("div", {"class": "story-body"}).get_text()
				except:
					print("No content found")
			s = Story(source=story, content=content)
			s.save()

		else: print("Already in DB")
		# print("story:", story)
		
	stories_add = Story.objects.all()
	output = ' '.join([i.content for i in stories_add])
	output = "<br>".join(keywordsList(output))
	# print(output)
	return HttpResponse(output)