import os
import django
from django.utils import timezone
import nltk
import praw
from sentiment import naivebayes
from praw.models import MoreComments
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from relationships.models import Story, Node, Edge, Sentiment

pos_lex = naivebayes.generate('sentiment/pos.txt', naivebayes.lexicon())
neg_lex = naivebayes.generate('sentiment/neg.txt', naivebayes.lexicon())
r = praw.Reddit(client_id='l-Gz5blkt7GCUg',
                client_secret='_xLEgNing89k6__sWItU1_j9aR8',
                user_agent='testscript by /u/pbexe')


def submission_sentiment(id):
    total = 0
    n = 0
    submission = r.submission(id)
    for top_level_comment in submission.comments:
        n += 1
        if isinstance(top_level_comment, MoreComments):
            continue
        total += naivebayes.sentiment(top_level_comment.body, pos_lex, neg_lex)
        return total / n


def stories():
    stories = []
    subreddits = ['news', 'worldnews', 'TrueNews', 'neutralnews']
    for subreddit in subreddits:
        submissions = r.subreddit(subreddit).top(limit=100)
        for item in submissions:
            sentiment = submission_sentiment(item.id)
            print(sentiment)
            stories.append((item.url, item.title, sentiment))
        submissions = r.subreddit(subreddit).hot(limit=100)
        for item in submissions:
            print(sentiment)
            sentiment = submission_sentiment(item.id)
            stories.append((item.url, item.title, sentiment))
    for item in stories:
        yield item


# Tokenizes the input so it can be analysed
def prepareForNLP(text):
    # Split up the input into sentences
    sentences = nltk.sent_tokenize(text)
    # Split up the sentences into words
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    # Tokenize the words
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
                edge = Edge(source=story, origin=node, destination=i)
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
            node = Node(name=kw, date=timezone.now(), collectedFrom=s)
            node.save()
        else:
            node = Node.objects.filter(name=kw)[0]
            node.date = timezone.now()
        node_sentiment = Sentiment(sentiment=story[2], node=node)
        node_sentiment.save()
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
        else:
            pass


if __name__ == "__main__":
    print("Updating DB")
    updateDB()
