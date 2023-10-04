from pwn import *

host = "2048.challs.olicyber.it"
port = 10007

r = remote(host, port)
print(r.recvuntil(b":"))

q = log.progress("Question: ")
ans = log.progress("Answer: ")

def computeAnswer(type, arg1, arg2):
    operations = {
        "SOMMA": lambda a, b: a + b,
        "DIFFERENZA": lambda a, b: a - b,
        "PRODOTTO": lambda a, b: a * b,
        "DIVISIONE": lambda a, b: a / b,
        "POTENZA": lambda a, b: a ** b,
        "DIVISIONE_INTERA": lambda a, b: a // b,
    }
    return operations[type](arg1, arg2)


for i in range (0,2048): 
    question = r.recv().decode("utf-8").strip()
    q.status(str(i) + ":"+question)
    if (len(question) == 0):
        print("Error "+ r.recv().decode("utf-8"))
        break
    #q.status(question)
    split = question.split(" ")
    answer = computeAnswer(split[0], int(split[1]), int(split[2]))
    ans.status(str(answer))
    r.send(str(answer).encode("utf-8") + b"\n")
print(r.recv().decode("utf-8"))

