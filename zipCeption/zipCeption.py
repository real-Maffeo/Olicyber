import os
from pwn import *

filename = "flag"
l = log.progress("Unzipping")


os.system("pwd")

for i in range (3000, 0, -1): 
    os.system("unzip flag" + str(i) + ".zip")
    os.system("rm flag" + str(i) + ".zip")
    l.status(str(i))

