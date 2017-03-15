"""Render the views
"""
from django.shortcuts import render
from django.http import HttpResponse
from .models import Node, Edge, Sentiment
import json
from numpy import interp


def ajax(request):

    """Returns a JSON object to the client containing all the nodes and edges

    Args:
        request (obj): The request made to the server

    Returns:
        obj: HTTP response containing the JSON
    """

    edges = Edge.objects.all()
    nodes = Node.objects.all()
    nodeList = []
    edgeList = []
    for node in nodes:
        if node.recent():
            n = 0
            total = 0
            for obj in Sentiment.objects.filter(node=node):
                if obj.sentiment is not None:
                    n += 1
                    total += obj.sentiment

            avg = total / n if n > 0 else 0.6
            avg = interp(avg, [0, 0.8], [0, 1])
            toAdd = {}
            toAdd['name'] = node.name
            toAdd['sentiment'] = avg if avg <= 1 else 1
            nodeList.append(toAdd)
    for edge in edges:
        if edge.recent():
            toAdd = {}
            toAdd['source'] = edge.origin.name
            toAdd['target'] = edge.destination.name
            toAdd['origin'] = edge.source
            edgeList.append(toAdd)
    jsonOut = {}
    jsonOut['links'] = edgeList
    jsonOut['nodes'] = nodeList

    return HttpResponse(json.dumps(jsonOut))


def index(request):

    """Return the index html file

    Args:
        request (obj): The request made to the server

    Returns:
        obj: Render object used to render `main.html`
    """

    return render(request, 'relationships/main.html')
