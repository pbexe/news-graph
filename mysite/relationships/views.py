from django.shortcuts import render
from django.http import HttpResponse
from .models import Story, Node, Edge
import json

def ajax(request):
	edges = Edge.objects.all()
	nodes = Node.objects.all()
	nodeList = []
	edgeList = []
	for node in nodes:
		tempDict = {}
		tempDict['name'] = node.name
		nodeList.append(tempDict)
	for edge in edges:
		tempDict = {}
		tempDict['source'] = edge.origin.name
		tempDict['target'] = edge.destination.name
		edgeList.append(tempDict)
	jsonOut = {}
	jsonOut['nodes'] = nodeList
	jsonOut['links'] = edgeList
	return HttpResponse(json.dumps(jsonOut))

def index(request):
	return render(request, 'relationships/main.html')