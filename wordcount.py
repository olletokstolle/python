"""
Counts the occurence of words in a text file and saves the result in a database.
"""

import codecs
import sqlite3
import string
import os

def init(db_name):

    """Connects to the database and creates a table if needed."""

    if os.path.isfile(db_name):
        create = False
    else:
        create = True

    global db
    db = sqlite3.connect(db_name)

    global cursor
    cursor = db.cursor()

    if create:
        cursor.execute('''CREATE TABLE words(word TEXT, count INT) ''')
        db.commit()

def strip_punctuation(filename):

    """Strips punctuation from the input file."""

    remove = dict.fromkeys(map(ord, string.punctuation))

    with codecs.open(filename,"r+", "utf-8") as file:
        rawtext = file.read()
        output = rawtext.translate(str.maketrans("","", string.punctuation))
        file.seek(0)
        file.write(output)
        file.truncate()

def count_words(filename):

    """Reads the input file and does the counting."""

    with codecs.open(filename,"r+", "utf-8") as file:
        wordcount = {}

        for word in file.read().split():
            word = word.lower()
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1

    for k,v in wordcount.items():
        cursor.execute('''INSERT INTO words(word, count) VALUES(?, ?)''', (k.lower(), v))
        db.commit()

def get_word_occurence(word):

    """
    Returns the occurence of a specific word in the database.
    If fed a string with more than one word it will count all given words separately.
    """

    word = word.lower()
    result_str = "\n Your chosen word '{}' is encountered {} times in the text."
    noresult_str = "\n The word '{}' is not found."

    if len(word.split(" ")) == 1:
        cursor.execute('''SELECT * FROM words WHERE word = ?''', (word,))
        results = cursor.fetchone()

        if results:
            print(result_str.format(results[0], str(results[1])))
        else:
            print(noresult_str.format(word))

    elif len(word.split(" ")) > 1:
        for w in word.split(" "):
            cursor.execute('''SELECT * FROM words WHERE word = ?''', (w,))
            results = cursor.fetchone()

            if results:
                print(result_str.format(results[0], str(results[1])))
            else:
                print(noresult_str.format(word))

def close_db():

    """For proper closing!"""

    db.close()

if __name__ == "__main__":

    pass
