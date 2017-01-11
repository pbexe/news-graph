# Import the library needed to interact with the operating system
import os

# Set the environment to Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

# Import the core Django library
import django

# Setup Django
django.setup()

# Import the timezone library to timestamp entries into the DB
from django.utils import timezone

# Import BeautifulSoup4 to clean the web pages
from bs4 import BeautifulSoup

# Import the DB tables
from relationships.models import Story, Node, Edge

# Import the library to access the RSS feeds
import feedparser

# Import the natural language toolkit to tokenize the scraped text
import nltk

# Import the library needed to interact with the outputs
import sys

import praw

def stories():
    stories = []
    news = feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml?edition=uk')
    for text in news.entries:
        stories.append((text.link, text.description))
    r = praw.Reddit(user_agent='Test Script by /u/bboe')
    subreddits = ['news', 'worldnews','TrueNews','neutralnews']
    for subreddit in subreddits:
        submissions = r.get_subreddit(subreddit).get_top(limit=100)
        for item in submissions:
            stories.append((item.url, item.title))
        submissions = r.get_subreddit(subreddit).get_hot(limit=100)
        for item in submissions:
            stories.append((item.url, item.title))
    for item in stories:
        yield item

# Tokenizes the input so it can be analysed
def prepareForNLP(text):
    # Split up the input into sentences
    sentences = nltk.sent_tokenize(text)
    # Split up the sentences into words
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    # Tokenize the 
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    # Return the split and tokenized sentences
    return sentences

def chunk(sentence):
    # Chunking pattern
    chunkToExtract = """
    NP: {<NNP>*}"""
    # Create the new parser
    parser = nltk.RegexpParser(chunkToExtract)
    # Parse the text
    result = parser.parse(sentence)
    # Yield the proper noun phrases
    for subtree in result.subtrees():
        if subtree.label() == 'NP':
            t = subtree
            t = ' '.join(word for word, pos in t.leaves())
            yield t

# Yields the keywords (NNPs) from the input as tuples
def keywords(text):
    sentences = prepareForNLP(text)
    for sentence in sentences:
        for kw in chunk(sentence):
            yield kw

def makeEdges(nodes, story):
    while True:
        if len(nodes) > 0:
            node = nodes[0]
            nodes.remove(node)
            for i in nodes:
                edge = Edge(source=story,origin=node,destination=i)
                edge.save()
        else:
            break

def addStory(story):
    print("Adding story:", story[0])
    s = Story(source=story[0], content=story[1])
    s.save()
    nodes = []
    for kw in keywords(story[1]):
        if len(Node.objects.filter(name=kw)) < 1:
            node = Node(name=kw,date=timezone.now(),collectedFrom=s)
            node.save()
        else:
            node = Node.objects.filter(name=kw)[0]
            node.date = timezone.now()
        nodes.append(node)
    makeEdges(nodes, story[0])

# Updates the DB to a more recent version of the news
def updateDB():
    # For each story currently on the BBC RSS feed
    for story in stories():
        # More than 0 if the story is in the DB
        matches = Story.objects.filter(source=story[0])
        # If the story isn't in the database
        if len(matches) == 0:
            addStory(story)
        else: pass

if __name__ == "__main__":
    print("Updating DB")
    updateDB()