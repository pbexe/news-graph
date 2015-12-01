from BBC.getStories import stories
from bs4 import BeautifulSoup
import urllib.request
import models.Story

for story in stories():
	s = Story(source=story)
	s.save()
	print("story:", story)
	with urllib.request.urlopen(story) as response:
		html = response.read()
		soup = BeautifulSoup(html, "html.parser")
		try:
			print(soup.find("div", {"class": "story-body"}).get_text())
		except:
			print("No content found")