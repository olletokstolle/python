"""
This program scrapes Workey.se, a swedish search engine for job advertisements. Feed it a list of keywords and it saves the amount of hits in a database file.
"""

from lxml import html
import requests
import time
import datetime
import sqlite3

def init(db_name):

    """Creates the database."""

    global db
    db = sqlite3.connect(db_name)

    global cursor
    cursor = db.cursor()

    cursor.execute('''CREATE TABLE results(keyword TEXT, hits INT, date TEXT) ''')
    db.commit()


def job_searcher(lst):

    """Does the actual searching/scraping."""

    today = datetime.date.today()

    for keyword in lst:
        url = requests.get('http://www.workey.se/lediga-jobb/med.' + keyword)
        tree = html.fromstring(url.text)
        amount = tree.xpath('//*[@id="search_results"]/div[1]/h1/text()')
        amount = str(amount[0]).split(' ', 1)[0]
        cursor.execute('''INSERT INTO results(keyword, hits, date) VALUES(?, ?, ?)''', (keyword, amount, today))
        db.commit()

        time.sleep(0.5)

    db.close()


if __name__ == '__main__':

    init("jobdb")

    #Example keywords.

    keywordlist = ['SQL', 'HTML', 'Python', 'PHP', 'Ruby on Rails', 'Ruby',
    'Django', 'Java', 'C++', 'Javascript', 'Shell', 'Objective C', 'Assembly',
    'Perl', 'ASP', 'Scala', 'Haskell', 'Clojure', 'Erlang', 'Linux', 'MySQL',
    'postgreSQL', 'mongoDB', 'noSQL', 'Oracle', 'Wordpress', 'CoffeeScript',
    'MATLAB', 'JSON', 'AJAX', 'Arduino', 'Delphi', 'XML', 'CSS', 'SEO', 'jQuery',
    'MVC', 'node.js', 'bash', 'Scrum', 'Hadoop']

    job_searcher(keywordlist)

