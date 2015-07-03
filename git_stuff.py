import subprocess
import time

def git_combo(filename, commit_message):

    user = ""
    pwd = ""


    subprocess.call('git add '+filename, shell=True)
    time.sleep(5)
    subprocess.call('git commit -m "'+commit_message+'"', shell=True)
    time.sleep(5)
    subprocess.call("git push -u origin master", shell=True)
    time.sleep(5)


if __name__ == '__main__':
    git_combo("git_stuff.py", "test commit")


