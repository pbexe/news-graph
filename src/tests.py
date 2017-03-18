"""Tests for updateDB.py and associated files.
"""
from django.test import TestCase
from relationships.models import Story, Node, Edge, Sentiment
from sentiment import naivebayes
import updateDB
import praw
from wikiapi import WikiApi
from django.utils import timezone


class SentimentTestCase(TestCase):

    """Test case used to test the sentiment analysis.

    Attributes:
        neg_lex (dict): Lexicon of negative sentiment and relative frequencies.
        pos_lex (dict): Lexicon of negative sentiment and relative frequencies.
    """

    def setUp(self):

        """Run setup required for the sentiment tests to run
        """

        self.pos_lex = naivebayes.generate('sentiment/pos.txt', naivebayes.lexicon())
        self.neg_lex = naivebayes.generate('sentiment/neg.txt', naivebayes.lexicon())

    def test_sentence_sentiment(self):

        """Test the sentiment of sentences
        """

        self.assertTrue(naivebayes.sentiment('That was terrible. I hated it.', self.pos_lex, self.neg_lex) < 0.5)
        self.assertTrue(naivebayes.sentiment('That was amazing. I loved it.', self.pos_lex, self.neg_lex) > 0.5)


class RedditTestCase(TestCase):

    """Test the interactions with Reddit

    Attributes:
        r (obj): Object used to interact with reddit. See https://pypi.python.org/pypi/praw
    """

    def setUp(self):

        """Setup the Reddit client
        """

        self.r = praw.Reddit(client_id='l-Gz5blkt7GCUg',
                             client_secret='_xLEgNing89k6__sWItU1_j9aR8',
                             user_agent='testscript by /u/pbexe')

    def test_article_fetching(self):

        """Test the fetching of an article to insure that the connection to reddit is set up as expected
        """

        submission = self.r.submission('5nbxbh')
        self.assertEqual(submission.title, '"Leave the internet and come play with me."')


class UpdateDBFunctionTests(TestCase):

    """Summary

    Attributes:
        neg_lex (dict): Lexicon of negative sentiment and relative frequencies.
        pos_lex (dict): Lexicon of negative sentiment and relative frequencies.
        node1 (obj): Object representing a node in the database
        node2 (obj): Object representing a node in the database
        node3 (obj): Object representing a node in the database
        r (obj): Object used to interact with reddit. See https://pypi.python.org/pypi/praw
        story (obj): Object representing a story in the database
        test_sentence (str): Sentence used for testing against
        test_sentence_tokenized (TYPE): A tokenized version of the test sentence
        test_sentence_with_entities (str): Sentence used for testing against that contains entities
        test_sentence_with_entities_nodes (list): The entities from the test sentence
        wiki (obj): Object used to interact with the Wikipedia API.
    """

    def setUp(self):

        """Set up all of the requirements for testing
        """

        self.pos_lex = naivebayes.generate('sentiment/pos.txt', naivebayes.lexicon())
        self.neg_lex = naivebayes.generate('sentiment/neg.txt', naivebayes.lexicon())
        self.wiki = WikiApi()
        self.r = praw.Reddit(client_id='l-Gz5blkt7GCUg',
                             client_secret='_xLEgNing89k6__sWItU1_j9aR8',
                             user_agent='testscript by /u/pbexe')
        self.test_sentence = 'The cat sat on the mat. The dog however, did not!'
        self.test_sentence_tokenized = [[('The', 'DT'),
                                         ('cat', 'NN'),
                                         ('sat', 'VBD'),
                                         ('on', 'IN'),
                                         ('the', 'DT'),
                                         ('mat', 'NN'),
                                         ('.', '.')],
                                        [('The', 'DT'),
                                         ('dog', 'NN'),
                                         ('however', 'RB'),
                                         (',', ','),
                                         ('did', 'VBD'),
                                         ('not', 'RB'),
                                         ('!', '.')]]
        self.test_sentence_with_entities = 'Dr Foster went to Glouster'
        self.test_sentence_with_entities_nodes = ['Dr Foster', 'Glouster']
        self.story = Story(source='http://example.com/', content='This is a title')
        self.story.save()
        self.node1 = Node(name='Key word 1', date=timezone.now(), collectedFrom=self.story)
        self.node1.save()
        self.node2 = Node(name='Key word 2', date=timezone.now(), collectedFrom=self.story)
        self.node2.save()
        self.node3 = Node(name='Key word 3', date=timezone.now(), collectedFrom=self.story)
        self.node3.save()

    def test_NLP_preparation(self):

        """Test the preparation done on sentences before NLP
        """

        self.assertListEqual(updateDB.prepareForNLP(self.test_sentence), self.test_sentence_tokenized)
        sentences = updateDB.prepareForNLP(self.test_sentence_with_entities)
        entities = []
        for sentence in sentences:
            for kw in updateDB.chunk(sentence):
                entities.append(kw)
        self.assertEqual(entities, self.test_sentence_with_entities_nodes)

    def test_make_edges(self):

        """Tests that edges between nodes can be correctly created
        """

        updateDB.makeEdges([self.node1, self.node2, self.node3], self.story)
        self.assertEqual(len(Edge.objects.all()), 3)

    def test_add_story(self):

        """Tests that stories can be added adn that all of the subsequent functions interact correctly
        """

        updateDB.addStory(('https://example.com/story/url', 'Mr Johnson has got a new cat called Dave', 0.8))
        self.assertEqual(len(Node.objects.filter(name='Dave')), 1)
        self.assertEqual(len(Story.objects.filter(source='https://example.com/story/url')), 1)
