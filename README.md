### What is it?

This is a series of tools written in Django by @pbexe to analyse different areas of the news and to build understanding of subsidiary aspects of this analysis.

### How do I run it?

To run the development server:
- Clone the project: `git clone https://github.com/pbexe/news-graph.git`
- Navigate to `manage.py`
- Build the DB: `python3 manage.py migrate`
- Update the DB: `python3 updateDB2.py`
- Run the server: `python3 manage.py runserver`

### Current tools

- Relationships (InDev)

### Dependencies
>To download all dependencies: `pip3 install --upgrade -r requirements.txt`

- Python 3
- Django 1.8 - `pip3 install Django`
- BeautifulSoup4 - `pip3 install beautifulsoup4`
- feedparser - `pip3 install feedparser`
- NLTK - `pip3 install nltk` followed by `python3 -m nltk.downloader book`.
