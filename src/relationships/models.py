# Import the library required to interact with the database
from django.db import models
# Import the library used for dates in Django
from django.utils import timezone

import datetime


# A class representing a table containing the Stories that have already been scrapped
class Story(models.Model):
    # The source of the news article
    source = models.URLField(max_length=1000)
    # The content of the news article
    content = models.TextField()
    date = models.DateTimeField('Date Collected', default=timezone.now)
    def recent(self):
        return self.date >= timezone.now() - datetime.timedelta(days=3)
    # A function to return the source of the news article when called
    def __str__(self):
        return self.source

# A class representing a table containing the nodes
class Node(models.Model):
    # The name of the node. ie: What it is representing
    name = models.CharField(max_length=50)
    # The date that the node was added to the database
    date = models.DateTimeField('Date Collected', default=timezone.now)
    # The news story that the node was  extracted from
    collectedFrom = models.ForeignKey(Story, related_name='story_collected_from', default="")
    def recent(self):
        return self.date >= timezone.now() - datetime.timedelta(days=3)
    # A function to return the name of the node when called
    def __str__(self):
        return self.name

# A class representing a table containing the nodes
class Edge(models.Model):
    # A link to the news article where the connection between the 2 nodes was made
    source = models.URLField(max_length=1000)
    # The node at which the edge starts
    origin = models.ForeignKey(Node, related_name='origin_node')
    # The node at which the edge ends
    destination = models.ForeignKey(Node, related_name='destination_node')
    date = models.DateTimeField('Date Collected', default=timezone.now)
    def recent(self):
        return self.origin.recent() and self.destination.recent()
    # A function to return the 2 nodes the edge joins when called
    def __str__(self):
        return str(self.origin) + " -> " + str(self.destination)