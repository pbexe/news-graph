from django.shortcuts import render
from django.http import HttpResponse
from .models import Node, Edge
import json


def ajax(request):
    edges = Edge.objects.all()
    nodes = Node.objects.all()
    nodeList = []
    edgeList = []
    for node in nodes:
        if node.recent():
            tempDict = {}
            tempDict['name'] = node.name
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
