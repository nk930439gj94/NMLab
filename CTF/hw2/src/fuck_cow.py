from base64 import b64encode, b64decode
from pwn import *

def getrecord():
    global socket
    a = socket.recv().decode().split('\n')
    i = 1
    s = ''
    while( True ):
        if a[i][:2] == ' -':
            break
        s += a[i].split()[1]
        i += 1
    return s.encode()
    

def bxor(b1, b2):
    result = bytearray()
    for b1, b2 in zip(b1, b2):
        result.append(b1 ^ b2)
    return bytes(result)


socket = remote('140.112.249.144', 60001)
socket.recv()
socket.sendline('save')
ct = b64decode( getrecord() )

# find IV
pattern = ct[16:32] + ct[:16]
IV_m = b''
for i in range(16):
    for j in range(256):
        pattern = pattern[:(15-i)] + bytes( [j] ) + pattern[(16-i):]
        socket.sendline( 'load ' + b64encode( pattern ).decode() )
        socket.recvuntil('(')
        eye = socket.recv(1)
        socket.recv()
        if eye == b'*':
            print( i )
            break
    IV_m = bytes( [ (i+1)^j ] ) + IV_m
    pattern = pattern[:(15-i)] + bxor( bytes( [i+2]*(i+1) ), IV_m ) + pattern[16:]

IV = bxor( b'{"milk": 0, "nam', IV_m )


socket.sendline( 'rename ' + '1'*11 )
socket.recv()
socket.sendline( 'save' )
ct = b64decode( getrecord() )

message = bxor( bxor( IV, b'{"milk": -1, "na' ), ct[16:32] )
motherfucker = codecs.encode( message.decode('ISO-8859-1'), "unicode_escape" )

socket.sendline( 'rename ' + '1'*11 + motherfucker.decode() )
socket.recv()
socket.sendline( 'save' )
ct = b64decode( getrecord() )

golden_ct = ct[32:48]

message = bxor( bxor( golden_ct, b'me": "admin"}\x03\x03\x03' ), ct[16:32] )
motherfucker = codecs.encode( message.decode('ISO-8859-1'), "unicode_escape" )

socket.sendline( 'rename ' + '1'*11 + motherfucker.decode() )
socket.recv()
socket.sendline( 'save' )
ct = b64decode( getrecord() )

golden_ct += ct[32:48]

socket.sendline( 'load ' + b64encode( golden_ct ).decode() )

socket.interactive()
