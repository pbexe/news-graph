import feedparser
d = feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml?edition=uk')
for item in d.entries:
	print(item['link'])
