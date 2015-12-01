from django.db import models

# Create your models here.
# Import the library required to interact with the database
from django.db import models

# A class representing a table containing the nodes
class Node(models.Model):
    # The name of the node. ie: What it is representing
    name = models.CharField(max_length=50)
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
    # A function to return the 2 nodes the edge joins when called
    def __str__(self):
        return str(self.origin) + " -> " + str(self.destination)

class Story(models.Model):
    source = models.URLField(max_length=1000)
    def __str__(self):
        return source