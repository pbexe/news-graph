from django.test import TestCase
from .models import Node, Edge, Sentiment, Story
from django.utils import timezone
import datetime
from django.urls import reverse


class DatabaseTestCases(TestCase):
    """Test cases to check that the database it functioning correctly"""
    def setUp(self):
        s = Story(source='http://example.com/', content='This is a title')
        s.save()
        node = Node(name='Key word', date=timezone.now(), collectedFrom=s)
        node.save()

    def test_database_functions(self):
        story = Story.objects.get(source='http://example.com/')
        node = Node.objects.get(name='Key word')
        self.assertEqual(story.content, 'This is a title')
        self.assertEqual(node.collectedFrom, story)

    def test_database_recent_with_old_time(self):
        time = timezone.now() - datetime.timedelta(days=100)
        old_story = Story(source='http://example.com/2/', content='This is also title', date=time)
        self.assertIs(old_story.recent(), False)

    def test_database_recent_with_new_time(self):
        time = timezone.now() - datetime.timedelta(days=1)
        new_story = Story(source='http://example.com/2/', content='This is also title', date=time)
        self.assertIs(new_story.recent(), True)

    def test_human_readable_output(self):
        story = Story.objects.get(source='http://example.com/')
        self.assertEqual(story.__str__(), 'http://example.com/')


class ViewTestCases(TestCase):
    def setUp(self):
        s = Story(source='http://example.com/', content='This is a title')
        s.save()
        node1 = Node(name='Key word', date=timezone.now(), collectedFrom=s)
        node1.save()
        node2 = Node(name='Key word', date=timezone.now(), collectedFrom=s)
        node2.save()
        link = Edge(source=s, origin=node1, destination=node2)
        link.save()

    def test_home_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'relationships/main.html' )

    def test_ajax_view(self):
        response = self.client.get(reverse('ajax'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '"name": "Key word"')
