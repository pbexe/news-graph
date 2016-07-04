### What is it?

This is a series of tools written in Django by @pbexe to analyse different areas of the news and to build understanding of subsidiary aspects of this analysis.

### How do I run it?

To run the development server:
- Clone the project: `git clone https://github.com/pbexe/news-graph.git`
- Navigate to `manage.py`
- Install the dependencies `pip3 install -r requirements.txt`
- Run `python3 install.py`
- Build the DB: `python3 manage.py migrate`
- Update the DB: `python3 updateDB2.py`
- Run the server: `python3 manage.py runserver 0.0.0.0:8000`

### Current tools

- Relationships (InDev)
