from bs4 import BeautifulSoup
import urllib
html = urllib.urlopen('http://www.nytimes.com/2009/12/21/us/21storm.html').read()
soup = BeautifulSoup(html)
texts = soup.findAll(text=True)

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True

visible_texts = filter(visible, texts)