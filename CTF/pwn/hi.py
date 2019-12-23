from pwn import *



obj = remote('140.112.249.144', 60000)
s = obj.recvuntil('^')
s = obj.recvuntil('\n')
max = int(s)
print('Max:', max)

lowerbound = 0
upperbound = 1 << max
guess = upperbound >> 1

counter = 0

while( True ):
    s = obj.recv()
    obj.sendline( str(guess) )
    s = obj.recvuntil(' ')
    s = obj.recv(1)
    counter += 1
    if( s == b'b' ):
        print( counter )
        upperbound = guess
        guess = ( lowerbound + guess ) >> 1
    elif( s == b's' ):
        print( counter )
        lowerbound = guess
        guess = ( upperbound + guess ) >> 1
    else:
        break

obj.interactive()