"""Models of data to be stored in the database
"""
from django.db import models
from django.utils import timezone
import datetime


class Story(models.Model):

    """Model to store each news story retrieved

    Attributes:
        content (obj): Object to describe story content
        date (obj): Object to describe date `Story` was retrieved
        source (obj): Object to describe the source of `Story`
    """

    source = models.URLField(max_length=1000)
    content = models.TextField()
    date = models.DateTimeField('Date Collected', default=timezone.now)

    def recent(self):

        """Returns whether `self` is recent

        Returns:
            bool: Was `self` recent?
        """

        return self.date >= timezone.now() - datetime.timedelta(days=3)

    def __str__(self):

        """Returns a string when the object is referred to

        Returns:
            str: The source of `Story`
        """
        return self.source


class Node(models.Model):

    """Model to store each node in the graph

    Attributes:
        collectedFrom (obj): Object to describe which `Story` the node was retrieved from
        date (obj): Object to describe when the node was created and last updated
        name (obj): Object to describe the name of the node
    """

    name = models.CharField(max_length=50)
    date = models.DateTimeField('Date Collected', default=timezone.now)
    collectedFrom = models.ForeignKey(Story, related_name='story_collected_from', default="")

    def recent(self):

        """Returns whether `self` is recent

        Returns:
            bool: Was `self` recent?
        """

        return self.date >= timezone.now() - datetime.timedelta(days=3)

    def __str__(self):

        """Returns a string when the object is referred to

        Returns:
            str: The `name` of the `Node`
        """

        return self.name


class Edge(models.Model):

    """Model to store each edge in the graph

    Attributes:
        date (obj): Object to describe the date when the edge was created
        destination (obj): Object to describe the destination of the edge
        origin (obj): Object to describe the origin `Node` of the edge
        source (obj): Object to describe the source `Node` of the edge
    """

    source = models.URLField(max_length=1000)
    origin = models.ForeignKey(Node, related_name='origin_node')
    destination = models.ForeignKey(Node, related_name='destination_node')
    date = models.DateTimeField('Date Collected', default=timezone.now)

    def recent(self):

        """Returns whether `self` is recent

        Returns:
            bool: Was `self` recent?
        """

        return self.origin.recent() and self.destination.recent()

    def __str__(self):

        """Returns a string when the object is referred to

        Returns:
            str: The `origin` and `destination` of `Edge`
        """

        return str(self.origin) + " -> " + str(self.destination)


class Sentiment(models.Model):

    """Model to describe the sentiment of each `Node`

    Attributes:
        node (obj): Object to describe the `Node` to which the sentiment is associated
        sentiment (obj): Object to describe the found sentiment of the `Node`
    """

    sentiment = models.FloatField(null=True, blank=True, default=None)
    node = models.ForeignKey(Node, related_name='sentiment_collected_from')

    def __str__(self):

        """Returns a string when the object is referred to

        Returns:
            str: The `sentiment` of `Sentiment`
        """

        return str(self.sentiment)
