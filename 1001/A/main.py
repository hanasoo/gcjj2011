# -*- coding: utf-8 -*-

#FILE_NAME = 'data'
#FILE_NAME = 'A-small-attempt0'
FILE_NAME = 'A-large'
IN_FILE = FILE_NAME + '.in'
OUT_FILE = FILE_NAME + '.out'

f = open(IN_FILE, 'r')
src = f.read().split('\n')
f.close()

t = int(src.pop(0))

#[5, 1]
#length , start

#1234567890   [10, 1] cut 3,4
#123 4567 890 [3, 1][4, 4][3, 8]
#4567 123 890 [4, 4][3, 1][3, 8] cut 3, 3
#456 7 12 3 890 [3, 4][1, 7][2, 1][1, 3][3, 8]

# 45678 -> 45 678
# dev([5, 4], 2) -> [2, 4][3, 6]
def dev(d, a):
	print 'dev %s, %s' % (d, a)
	return [d[0], a],[a+d[0], d[1]-a]

#print dev([10, 1] , 3)

# 1234567890 -> 123 4567 890
# cut([[10, 1]],3,4) -> [3, 1][4, 4][3, 8]
def cut(ds, a, b):
	count = 0
	result = []
	picked = []
	aend = False
	bend = False
	for i in range(len(ds)):
		d = ds[i]
		s = d[0]
		l = d[1]
		if l == 0:
			continue
		if not aend and a < count + l:
			f, r = dev(d, a - count)
			result.append(f)
			aend = True
			if a + b <= count + l:
				rf, rr = dev(r, b)
				picked.append(rf)
				result.append(rr)
				bend = True
			else:
				picked.append(r )
		elif aend and not bend:
			if a + b <= count + l:
				f, r = dev(d, a+b - count)
				picked.append(f)
				result.append( r)
				bend = True
			else:
				picked.append(d)
		else:
			result.append(d)
		count = count + l
	return picked + result

#print cut([[10, 1]], 3, 4)
#exit()

def search(ds, w):
	count = 0
	for d in ds:
		if w <= count + d[1]:
			return d[0] + w - count - 1
		count = count + d[1]
	return 0

result = ""
print('############ start #################')
for i in range(t):
	print('############ start %d ###################' % i)
	m, c, w = map(lambda x: int(x), src.pop(0).strip().split(' '))
	#deck = range(1, m + 1)
	
	ds = [[1, m]]
	#print deck
	for j in range(c ):
		a, b = map(lambda x: int(x), src.pop(0).strip().split(' '))
		a = a - 1
		print '%d %d' % (a, b)
		#print '%s %s %s' % (deck[a:a+b], deck[0:a], deck[a+b:])
		#deck = deck[a:a+b] + deck[0:a] + deck[a+b:]
		#print deck
		
		ds = cut(ds, a, b)
		
		print ds
		
	#print '%d is %d' % (w, deck[w - 1])
	print '%d is %d' % (w, search(ds, w))
	result = result + 'Case #%d: %d\n' % (i + 1, search(ds, w))
	
print('############ end ###################')


f = open(OUT_FILE, 'w')
f.write(result)
f.close()


