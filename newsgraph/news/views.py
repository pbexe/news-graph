from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from bs4 import BeautifulSoup
import urllib.request
from .models import Story, Node, Edge
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

def updateDB():
	for story in stories():
		matches = Story.objects.filter(source=story)
		if len(matches) == 0:
			print("Adding story:", story)
			content = ""
			with urllib.request.urlopen(story) as response:
				html = response.read()
				soup = BeautifulSoup(html, "html.parser")
				if soup != "":
					for junk in soup(["script", "style", "img"]):
					    junk.extract()
					content = soup.find("div", {"class": "story-body"}).get_text()
				else:
					print("No content found")
			s = Story(source=story, content=content)
			s.save()
			for kw in keywords(content):
				DBalready = []
				if kw not in DBalready:
					DBalready.append(kw)
					node = Node(name=kw,date=timezone.now(),collectedFrom=s)
					node.save()
		else: print("Already in DB")


def index(request):
	updateDB()
	node_add = Node.objects.all()
	output = '<br />'.join([i.name for i in node_add])
	# print(output)
	return HttpResponse(output)