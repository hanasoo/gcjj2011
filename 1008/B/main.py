# -*- coding: utf-8 -*-

FILE_NAME = 'data'
FILE_NAME = 'B-small-attempt0'
#FILE_NAME = 'A-large'
IN_FILE = FILE_NAME + '.in'
OUT_FILE = FILE_NAME + '.out'

f = open(IN_FILE, 'r')
src = f.read().split('\n')
f.close()

T = int(src.pop(0))

result = ""
print('############ start #################')
for i in range(T):
	print('############ try %d ###################' % i)
	A, B, C = map(lambda x: int(x), src.pop(0).strip().split(' '))
	
	print A
	x = A
	r = A
	for j in range(B):
		skip = []
		r = pow(r, x) % C
		x = pow(x, x)
		print r
	r = r % C
	
	print '%d mod %d' % (r, C)
	result = result + 'Case #%d: %d\n' % (i + 1, r)
	
print('############ end ###################')


f = open(OUT_FILE, 'w')
f.write(result)
f.close()


