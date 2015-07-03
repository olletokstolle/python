import subprocess
import time
import argparse

def git_combo(filename, commit_message):

    #Lazy stuff.

    subprocess.call('git add '+filename, shell=True)
    subprocess.call('git commit -m "'+commit_message+'"', shell=True)
    subprocess.call("git push -u origin master", shell=True)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Git add-commit-push combo script.')
    parser.add_argument("file", help="file name.", type=str)
    parser.add_argument("commit", help="commit message", type=str)

    args = parser.parse_args()

    git_combo(args.file, args.commit)


