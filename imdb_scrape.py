import requests
from bs4 import BeautifulSoup
import sqlite3
import os

"""
Scraper for imdb. Collects info (title, year, rating, amount of votes) on all directed films of a given director. Saves the results in a sqlite database.
"""


def init(db_name):

    #Connects to the database and creates a table if needed.

    if os.path.isfile(db_name):
        create = False
    else:
        create = True

    global db
    db = sqlite3.connect(db_name)

    global cursor
    cursor = db.cursor()
    
    if create:
        cursor.execute('''CREATE TABLE dir(director TEXT, title TEXT, year INT, rating FLOAT, users TEXT) ''')
        db.commit()


def scrape_director(imdb_id):

    #Collects the info. The string imdb_id is the last part of the url. For example Christopher Nolan has the id "nm0634240" (full url: http://www.imdb.com/name/nm0634240).

    url = "http://www.imdb.com/name/" + imdb_id

    get = requests.get(url)
    data = get.text
    soup = BeautifulSoup(data)

    name = soup.select('#overview-top > h1 > span.itemprop')[0].get_text()
    data2 = soup.findAll('div',attrs={'class':'filmo-category-section'});
    filmlist = []

    for div in data2:
        links = div.findAll('a')
        for a in links:
            filmurl = 'http://imdb.com' + a['href']
            if filmurl not in filmlist and '_dr_' in filmurl:
                filmlist.append(filmurl)
                getfilm = requests.get(filmurl)
                data3 = getfilm.text
                soup2 = BeautifulSoup(data3)
                try:
                
                    titles = soup2.select('#overview-top > h1')
                    titles2 = titles[0].get_text().split(' ', 1)[1].translate(str.maketrans('()','  '))
                    title = titles2.split('\n')[0]
                    year = titles2.split('\n')[1].strip()
                    rating = soup2.select('#overview-top > div.star-box.giga-star > div.titlePageSprite.star-box-giga-star')[0].get_text()
                    users = soup2.select('#overview-top > div.star-box.giga-star > div.star-box-details > a')[0].get_text().split(' ')[1].replace(',', '')
                    cursor.execute('''INSERT INTO dir(director, title, year, rating, users) VALUES(?, ?, ?, ?, ?)''', (name, title, year, rating, users ))
                    db.commit()
                    print("Scraped: " + title)
                    
                except IndexError:
                    pass
            

def close_db():

    #For proper closing!

    db.close()


if __name__ == "__main__":

    pass
