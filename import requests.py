import requests
import re

url = "http://roller.challs.olicyber.it/get_flag.php"


r = requests.get(url, allow_redirects=False)

print(re.findall(r'flag{.*}', r.text)[0])