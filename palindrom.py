#!/usr/bin/env python

"""
196-algoritmen.

https://sv.wikipedia.org/wiki/196-algoritmen

"""

def main():
    while True:
        n = input("Skriv det nummer du vill palindrom-räkna med: ")
        if len(n) < 2:
            print("Numret måste vara tvåsiffrigt eller längre. \n")
            continue
        else:
            its = 0
            n = int(n)
            while True:
                n += int(str(n)[::-1])
                its += 1
                if str(n) == str(n)[::-1]:
                    print("Palindromnummer {} hittat efter {} iteration(er)! \n".format(n,its))
                    break

if __name__ == '__main__':
    main()
