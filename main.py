from BBC.getStories import stories
from bs4 import BeautifulSoup
import urllib.request

for story in stories():
	print("story:", story)
	with urllib.request.urlopen(story) as response:
		html = response.read()
		soup = BeautifulSoup(html, "html.parser")
		try:
			print(soup.find("div", {"class": "story-body"}).get_text())
		except:
			print("No content found")
		
