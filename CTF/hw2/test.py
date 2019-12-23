from base64 import b64encode, b64decode
from pwn import *
import codecs
import random

s = b'H2\xda\x11\x0cI9\x12H\x97Vv\xfcP\xeeQ>\x9d\xa6\x95\xdf1\xc9\x16\xc8\xbf\xba\xb7\x84\x02/7'
print( len(s) )
for i in range( len(s) ):
    print( s[i], end=' ' )
print()