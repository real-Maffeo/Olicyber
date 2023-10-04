import requests
import bs4
from fake_useragent import UserAgent

scoreboardUrl = "https://training.olicyber.it/scoreboard"

loginUrl = "https://training.olicyber.it/login"

r = requests.session()



loginData = {
    "email":"sergiocibecchini.productivity@gmail.com",
    "password":"HJL4Pd&4q26$D8B@"
}
headers = {'User-Agent': str(UserAgent().chrome)}
r.get(scoreboardUrl, headers=headers)
answ = r.post(loginUrl,  headers=headers, data=loginData)

print(answ.text)

soup = bs4.BeautifulSoup(answ.text, 'html.parser')

scoreTable =  soup.find('table', {'class': 'm-0 text-nowrap table table-striped table-bordered table-hover'})

placeScoreDict = {}

print(scoreTable)

