from django.test import TestCase
from relationships.models import Story, Node, Edge, Sentiment
from sentiment import naivebayes
import updateDB
import praw


class SentimentTestCase(TestCase):
    def setUp(self):
        self.pos_lex = naivebayes.generate('sentiment/pos.txt', naivebayes.lexicon())
        self.neg_lex = naivebayes.generate('sentiment/neg.txt', naivebayes.lexicon())

    def test_sentence_sentiment(self):
        self.assertTrue(naivebayes.sentiment('That was terrible. I hated it.', self.pos_lex, self.neg_lex) < 0.5)
        self.assertTrue(naivebayes.sentiment('That was amazing. I loved it.', self.pos_lex, self.neg_lex) > 0.5)


class RedditTestCase(TestCase):
    def setUp(self):
        self.r = praw.Reddit(client_id='l-Gz5blkt7GCUg',
                             client_secret='_xLEgNing89k6__sWItU1_j9aR8',
                             user_agent='testscript by /u/pbexe')

    def test_article_fetching(self):
        submission = self.r.submission('5nbxbh')
        self.assertEqual(submission.title, '"Leave the internet and come play with me."')
        self.assertEqual(submission.comments[0].body.encode("utf-8"), 'How do you not play with that dog after that?')
