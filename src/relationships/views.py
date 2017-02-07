from django.shortcuts import render
from django.http import HttpResponse
from .models import Node, Edge, Sentiment
import json
from colour import Color


def ajax(request):
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
            tempDict = {}
            tempDict['name'] = node.name
            hue = (avg * 120)
            c = Color(hsl=(hue/360, 1, 0.5))
            tempDict['sentiment'] = c.hex
            nodeList.append(tempDict)
    for edge in edges:
        if edge.recent():
            tempDict = {}
            tempDict['source'] = edge.origin.name
            tempDict['target'] = edge.destination.name
            tempDict['origin'] = edge.source
            edgeList.append(tempDict)
    jsonOut = {}
    jsonOut['links'] = edgeList
    jsonOut['nodes'] = nodeList

    return HttpResponse(json.dumps(jsonOut))


def index(request):
    return render(request, 'relationships/main.html')
