from pwn import *
import hashlib

HOST = 'rabbit.challs.olicyber.it'
PORT = 10501
r = remote(HOST, PORT)

r.recvuntil(b'Execute:')
val = r.recv().decode().strip().split()

target = val[2]

i = 0
while True:
    h = hashlib.sha1(str(i).encode('ascii')).hexdigest()
    if h.endswith(target):
        r.sendline(str(i).encode())
        print('done')
        break

    i += 1
r.interactive()