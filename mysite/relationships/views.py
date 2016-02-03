from django.shortcuts import render
from django.http import HttpResponse
from .models import Story, Node, Edge

def index(request):
	# Get a list of all nodes
	edge_add = Edge.objects.all()
	output = ""
	# For each edge
	for edge in edge_add:
		# Add that edge to the output
		output += edge.origin.name
		output += " => "
		output += edge.destination.name
		output += "<br />"
	# Return the output to the client
	return HttpResponse(output)