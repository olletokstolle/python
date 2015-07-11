"""
omdb-API wrapper.

"""

import requests
import json

class Movie(object):

    def __init__(self, string):
        self.get_data(string)

    def get_data(self, string):

        """Fetch json-data."""

        get = requests.get("http://www.omdbapi.com/?t={}&y=&plot=short&r=json".format(string))
        json_data = json.loads(get.text)

        if json_data["Response"] == "True":
            self.results = True
            self.title = json_data["Title"]
            self.year = json_data["Year"]
            self.rating = json_data["imdbRating"]
            self.imdbvotes = json_data["imdbVotes"]
            self.plot = json_data["Plot"]
            self.runtime = json_data["Runtime"]
            self.director = json_data["Director"]
            self.writer = json_data["Writer"]
            self.actors = json_data["Actors"]
            self.genre = json_data["Genre"]
            self.country = json_data["Country"]
            self.language = json_data["Language"]
            self.poster = json_data["Poster"]
        else:
            self.results = False
            pass



if __name__ == '__main__':

    pass