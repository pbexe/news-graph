from django.contrib import admin

from .models import Node, Edge, Story, Sentiment

admin.site.register(Node)
admin.site.register(Edge)
admin.site.register(Story)
admin.site.register(Sentiment)
