#!/usr/bin/env python

"""
Movie lookup script.

Usage: ./movie_lookup.py [-v] title
"""

import argparse
import omdb

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Movie lookup script.')
    parser.add_argument("-v", help="Add this argument if you want even more info about the movie.", action="store_true")
    parser.add_argument("title", help="Movie title you want to search for.", type=str, nargs='*')

    args = parser.parse_args()

    if len(args.title) > 1:
        args.title = "".join([word+"+" for word in args.title])

    m = omdb.Movie(args.title)

    if m.results:
        if args.v:
            results = """{} ({})\n{}\nDirector: {}\nActors: {}\nRuntime: {}\nRating: {}"""
            results = results.format(m.title,m.year,m.plot,m.director,m.actors,m.runtime,m.rating)
            print(results)

        else:
            print("{} ({})\n{}\nRating: {}".format(m.title,m.year,m.plot,m.rating))
    else:
        print("No movie found.")
