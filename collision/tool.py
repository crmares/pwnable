from pwn import *
from os import *


payload = "\xC8\xCE\xC5\x06" * 4 + "\xCC\xCE\xC5\x06"


local = False

if local:
	io = os.system('./col' + ' ' +  payload)
else:
	shell = ssh('col', 'pwnable.kr', password='guest', port=2222)
	print shell['./col' + ' ' + payload]

