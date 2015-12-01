from django.shortcuts import render

from django.http import HttpResponse

from .models import Node

def index(request):
	nodes = Node.objects.all()
	output = ', '.join([i.name for i in nodes])
	print(output)
	return HttpResponse(output)