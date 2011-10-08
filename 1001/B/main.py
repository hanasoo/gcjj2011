# -*- coding: utf-8 -*-

FILE_NAME = 'data'
FILE_NAME = 'B-small-attempt0'
FILE_NAME = 'B-large'
IN_FILE = FILE_NAME + '.in'
OUT_FILE = FILE_NAME + '.out'

f = open(IN_FILE, 'r')
src = f.read().split('\n')
f.close()

class Coffee:
	day = 1
	def __init__(self, c, t, s):
		self.c = c
		self.t = t
		self.s = s
	def __str__(self):
		return 'c: %d, t: %d, s: %d' % (self.c, self.t, self.s)
	def __cmp__(self, o):
		return cmp(o.s, self.s)
	def is_avail(self):
		return self.day <= self.t
	def drink(self):
		print 'day: %d drink: %s' % (self.day, self)
		self.c = self.c - 1
		return self.s

T = int(src.pop(0))
result = ""
print('############ start #################')
for y in range(T):
	print('############ start %d ###################' % y)
	n, k = map(lambda x: int(x), src.pop(0).strip().split(' '))
	print 'n: %d, k: %d' % (n, k)
	mcs = []
	days = []
	for j in range(n):
		c, t, s = map(lambda x: int(x), src.pop(0).strip().split(' '))
		mcs.append(Coffee(c, t, s))
		days.append(t)
		print mcs[j]
	
	days.sort()
	days.reverse()
	
	cs = []
	sat = 0
	Coffee.day = k
	while(Coffee.day > 0):
	#for i in range(k, 0, -1):
		i = Coffee.day
		print i
		if i in days:
			print 'add'
			l = len(mcs)
			new_mcs = []
			for j in range(l):
				if mcs[j].is_avail():
					cs.append(mcs[j])
				else:
					new_mcs.append(mcs[j])
			mcs = new_mcs
			cs.sort()
			days.pop(0)
		if 0 < len(cs):
			sat = sat + cs[0].drink()
			if cs[0].c == 0:
				print 'delete %s' % cs[0]
				cs.pop(0)
		else:
			print 'no coffee'
			i = days[0] + 1
		Coffee.day = i - 1
	print 'res %d' % sat
	
	result = result + 'Case #%d: %d\n' % (y + 1, sat)
	
print('############ end ###################')


f = open(OUT_FILE, 'w')
f.write(result)
f.close()


