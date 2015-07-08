#!/usr/bin/env python

"""
Simple commit+push combo script.

Usage: python git_combo.py "commit message"
"""

import subprocess
import time
import argparse

def git_combo(commit_message):

    """Lazy stuff. Git commit+push combo."""

    subprocess.call('git add --all', shell=True)
    subprocess.call('git commit -a -m "'+commit_message+'"', shell=True)
    subprocess.call("git push -u origin master", shell=True)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Git script.')
    parser.add_argument("commit", help="commit message", type=str)

    args = parser.parse_args()

    git_combo(args.commit)


