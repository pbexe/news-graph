from django.shortcuts import render
from django.http import HttpResponse
from .models import Node, Edge, Sentiment
import json
from numpy import interp


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
            avg = interp(avg, [0, 0.8], [0, 1])
            tempDict = {}
            tempDict['name'] = node.name
            tempDict['sentiment'] = avg if avg <= 1 else 1
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
