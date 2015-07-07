#!/usr/bin/env python

import argparse

"""
Updates the table in my README.md.

Usage: python update_readme.py "filename" "description"

"""

def update_readme(filename, desc):

    with open("README.md", "a") as f:
        output ="| {} | {} |".format(filename,desc)
        f.write("\n"+output)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='README update')
    parser.add_argument("filename", help="filename", type=str)
    parser.add_argument("desc", help="description", type=str)

    args = parser.parse_args()

    update_readme(args.filename, args.desc)







