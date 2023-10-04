import requests
import bs4
import re
from pwn import *
url = "http://infinite.challs.olicyber.it/"

def makeRequest(): 
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    return soup

def getType(soup):
    question = soup.find('h2').text
    split = question.split(" ")
    return split[0]

def getQuestion (soup):
    question = soup.find('p').text
    return question

def solveGrammar (question): 
    split = question.split('"')
    letter = split[1]
    word = split[3]
    #number of letters in word
    res = len(re.findall(letter, word))
    data = {
        'letter': res
    }
    return data
def solveMath (question): 
    split = question.split(" ")
    num1 = int(split[2])
    split[4] = split[4].replace("?", "")
    num2 = int(split[4]) 
    res = num1 + num2
    data = {
        'sum': str(res)
    }
    return data
def solveArt (question): 
    split = question.split(" ")
    color = split[5].replace("?", "")
    return color+"="

r = requests.session()
soup = makeRequest()

q = log.progress("Question")
a = log.progress("Answer")
t = log.progress("Type")
c = log.progress("Count")
i = 0
while(True): 
    i+=1  
    c.status(i)
    type = getType(soup)
    question = getQuestion(soup)
    q.status(question)
    t.status(type)
    if type == "GRAMMAR":
        data = solveGrammar(question)
    elif type == "MATH":
        data = solveMath(question)
    elif type == "ART":
        data = solveArt(question)
    else: 
        print("Error")
    answ = r.post(url, data=data)
    a.status(str(data))
    if ("WRONG" in answ.text):
        print("WRONG")
        break
    elif ("flag" in answ.text):
        print("FLAG: "+answ.text)
        break
    soup = bs4.BeautifulSoup(answ.text, 'html.parser')
    


