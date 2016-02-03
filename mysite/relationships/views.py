from django.shortcuts import render
from django.http import HttpResponse
from .models import Story, Node, Edge

def index(request):
	# Get a list of all nodes
	edge_add = Edge.objects.all()
	output = """<style>table, th, td {
    border: 1px solid black;border-collapse: collapse;
	}</style>"""
	output += "<table>"
	# For each edge
	for edge in edge_add:
		output += '<tr>'
		# Add that edge to the output
		output += '<td>' + edge.origin.name + '</td>'
		output += '<td>' + edge.destination.name + '</td>'
		output += "</tr>"
	output += '</table>'
	# Return the output to the client
	return HttpResponse(output)