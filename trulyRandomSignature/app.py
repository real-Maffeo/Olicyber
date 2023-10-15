#!/usr/bin/env python3.8

from waitress import serve
from flask import Flask, request, make_response

import os
import hmac
import time
import hashlib
from datetime import datetime
import random
import string

flag = os.getenv("FLAG")

app = Flask(__name__)

def get_random_string(length):
  #restituisce una stringa di lunghezza length, in teroia randomica ma in priatica è seeddata con seed
  letters = string.ascii_lowercase
  result_str = ''.join(random.choice(letters) for i in range(length))
  return result_str

#uptime e il seed sono creati nello stesso momento, quindi il seed è sempre lo stesso
uptime = time.time()
seed = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
print(f"Seed: {seed}")
random.seed(seed)
SUPER_SECRET_KEY = get_random_string(32)
print(f"SUPER_SECRET_KEY: {SUPER_SECRET_KEY}")

#chiama sign su 'admin' e usando la SUPER_SECRET_KEY
def sign(text, key):
  textAsBytes = bytes(text, encoding='ascii')
  keyAsBytes  = bytes(key, encoding='ascii')
  signature = hmac.new(keyAsBytes, textAsBytes, hashlib.sha256)
  return signature.hexdigest()

#text non è altro che l'username, key è la SUPER_SECRET_KEY
def verify(text, signature, key):
  expected_signature = sign(text, key)
  #Quella giusta è semplicemente sign ('admin', SUPER_SECRET_KEY)
  return hmac.compare_digest(expected_signature, signature)

@app.route('/admin')
def admin():
  #cookie sarebbe l'username
  cookie = request.cookies.get('user')
  signature = request.cookies.get('signature')

  #il cookie è admin nel nostro caso, la signature è la signature di admin
  is_cookie_valid = verify(cookie, signature, SUPER_SECRET_KEY)

  if is_cookie_valid == False:
    return "HACKER DETECTED, ABORTING"

  if cookie == "admin":
    return f'Flag: {flag}'
  
  return "Hey, come va? Non c'è niente qui"

@app.route('/')
def index():
  default_user_name = "not_admin"

  resp = make_response(f"Ciao {default_user_name}!")
  #time.time() restituisce il tempo in secondi dall' epoch
  resp.headers['X-Uptime'] = str(int(time.time()-uptime))

  resp.set_cookie("user", value=default_user_name)
  resp.set_cookie("signature", value=sign(default_user_name, SUPER_SECRET_KEY))

  return resp

