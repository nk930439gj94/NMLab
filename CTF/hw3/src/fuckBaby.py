output = "$@^#?#!)~@(+@$*($(&$&~#!-=()!+!*-_)?_^+$(~$(&~&@%-$(*)?^_&%%!)~-#)-~^&^(&$&%~$_~"

def numeralize(a):
	temp = '~!@#$%^&*()_+=-?'
	for i in range(16):
		if temp[i] == a:
			return i

a = []
for i in range(len(output)):
	a.append(numeralize(output[i]))

b = []
for i in range(16):
	b.append(int((57*i)%16))


v4 = 0
ans = ''
for i in range(40):
	x = -b[v4] + a[i*2]
	if x < 0:
		x+=16

	v4 = a[i*2]

	y =  a[i*2+1] - b[v4]
	if y<0:
		y+=16

	v1 = 16*x + y 

	v4 = a[i*2+1]

	ans+=str(chr(v1))

print (ans)
		