"""
Simple multiple choice quiz program for answering questions. Could potentially be useful for studying, I guess.

Reads the questions from a .csv-file (semicolon delimited) with the following four columns:
id (just a number, use not yet implemented), question (the actual question), alts (the different choices), correct (correct choice number).

Example usage:
python quizzing.py philosophy.csv [-n number of questions]
"""

import csv
import random
import time
import os, sys
import argparse
import colorama
from colorama import Back, Fore

def init():

    #Just a fancy welcome to the quiz-thing.

    colorama.init()
    os.system("clear")

    print(Fore.MAGENTA + "\n Welcome to...")
    print(Fore.GREEN +"""
       ██████╗ ██╗   ██╗██╗███████╗
      ██╔═══██╗██║   ██║██║╚══███╔╝
      ██║   ██║██║   ██║██║  ███╔╝
      ██║▄▄ ██║██║   ██║██║ ███╔╝
      ╚██████╔╝╚██████╔╝██║███████╗
       ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝

        """)

def quiz(filename, num_questions=10):

    #The actual quiz.

    print(Fore.MAGENTA + " Questions pulled from {}. Number of questions to answer: {} \n".format(filename, num_questions))

    os.system("""bash -c 'read -s -n 1 -p " Press any key to start the quiz."'""")
    os.system("clear")

    score = 0

    with open(filename) as csv_object:
        reader = list(csv.DictReader(csv_object, delimiter=';'))

        for question in range(num_questions):
            row = random.choice(reader)
            print(" Question #{}:\n\n {} \n\n Choices:\n\n {} \n".format(question+1,row["question"],row["alts"]))
            answer = input(" Which number is correct? >> ")

            if answer == row["correct"]:
                score += 1
                print(Fore.BLACK + Back.GREEN +"\n Correct answer. Current score: {} ({}%)\n".format(score,round((score/(question+1)*100),2)))
            else:
                print(Fore.WHITE + Back.RED +"\n Incorrect answer. Current score: {} ({}%)\n".format(score,round((score/(question+1)*100),2)))

            print(Back.RESET+Fore.MAGENTA+"Continues in two seconds..")
            time.sleep(2)
            os.system("clear")

        print("\n Quiz finished. Final score: {} ({}% correct)\n".format(score,round((score/(question+1)*100),2)))
        os.system("""bash -c 'read -s -n 1 -p " Press any key to stop quizzing.\n"'""")
        sys.exit()




if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Quiz!')
    parser.add_argument("csvfile", help="csv-file with question data.", type=str)
    parser.add_argument("-n", help="number of questions", type=int)

    args = parser.parse_args()

    init()

    if args.n:
        quiz(args.csvfile,args.n)
    else:
        quiz(args.csvfile)

