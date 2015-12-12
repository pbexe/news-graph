from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from bs4 import BeautifulSoup
import urllib.request
from .models import Story, Node, Edge
import feedparser
import nltk
import sys

if sys.stdout.encoding != 'cp850':
  sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'strict')
if sys.stderr.encoding != 'cp850':
  sys.stderr = codecs.getwriter('cp850')(sys.stderr.buffer, 'strict')

# Returns a list of stories currently on the front page of the BBC website
def stories():
	# Connect to the BBC RSS feed
	news = feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml?edition=uk')
	# For every story
	for story in news.entries:
		# Return the link to that story
		yield story['link']

# Tokenizes the input
def prepareForNLP(text):
	sentences = nltk.sent_tokenize(text)
	sentences = [nltk.word_tokenize(sent) for sent in sentences]
	sentences = [nltk.pos_tag(sent) for sent in sentences]
	return sentences

def chunk(sentence):
	chunkToExtract = "NP: {<NNP>*<DT>?<NNP>*}"
	parser = nltk.RegexpParser(chunkToExtract)
	result = parser.parse(sentence)
	result.draw()

# Yields the keywords (NNPs) from the input as tuples
def keywords(text):
	sentences = prepareForNLP(text)
	for sentence in sentences:
		#chunk(sentence)
		for kw in chunk(sentence):
			yield kw

def chunk(sentence):
	chunkToExtract = """
	NP: {<NNP>*}
		# {<DT>?<JJ>?<NNS>}
		#{<NN>*<NP>*}
		#{<NP>*<NN>*}"""
	parser = nltk.RegexpParser(chunkToExtract)
	result = parser.parse(sentence)
	for subtree in result.subtrees():
		if subtree.label() == 'NP':
			t = subtree
			t = ' '.join(word for word, pos in t.leaves())
			yield t

# Returns the keywords (NNPs) from the input as a list of tuples
def keywordsList(text):
	output = []
	sentences = prepareForNLP(text)
	for sentence in sentences:
		for kw in chunk(sentence):
			output.append(kw)
	return output

def makeEdges(nodes, story):
	while True:
		if len(nodes) > 0:
			node = nodes[0]
			nodes.remove(node)
			for i in nodes:
				edge = Edge(source=story,origin=node,destination=i)
				edge.save()
				print(edge)
		else:
			break


def addStory(story):
	print("Adding story:", story)
	content = ""
	with urllib.request.urlopen(story) as response:
		html = response.read()
		soup = BeautifulSoup(html, "html.parser")
		if soup != "":
			for junk in soup(["script", "style", "img"]):
			    junk.extract()
			try:
				content = soup.find("div", {"class": "story-body"}).get_text()
			except:
				pass
		else:
			print("No content found")
	s = Story(source=story, content=content)
	s.save()
	content = content.replace(".", ". ")
	DBalready = []
	nodes = []
	for kw in keywords(content):
		if kw not in DBalready:
			DBalready.append(kw)
			node = Node(name=kw,date=timezone.now(),collectedFrom=s)
			nodes.append(node)
			node.save()
	makeEdges(nodes, story)

# Updates the DB to a more recent version of the news
def updateDB():
	# For each story currently on the BBC RSS feed
	for story in stories():
		# More than 0 if the story is in the DB
		matches = Story.objects.filter(source=story)
		# If the story isn't in the database
		if len(matches) == 0:
			addStory(story)
		else: print("Already in DB")


def index(request):
	updateDB()
	edge_add = Edge.objects.all()
	output = ""
	for edge in edge_add:
		output += edge.origin.name
		output += " -> "
		output += edge.destination.name
		output += "<br />"
	# print(output)
	return HttpResponse(output)