from pwn import *

host = "melody.challs.olicyber.it" 
port = 10020


nonce0 = "02"
right0 = b"0cce6bab87baa7031b69539ac1a211f202fc35cc8f3ac27fdb7e527527310f0e"

while (True): 
    r = remote(host, port)
    r.recvline()
    nonce = r.recvline().decode().strip()
    nonce = nonce.split(" ")[1]
    if (nonce == nonce0):
        r.sendline(right0)
        r.recvline()
        flag = r.recvline().decode().strip()
        print(flag)
        break
    else:
        r.close()
        continue




