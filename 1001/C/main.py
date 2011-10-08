# -*- coding: utf-8 -*-

FILE_NAME = 'data'
FILE_NAME = 'C-small-attempt0'
FILE_NAME = 'C-large'
IN_FILE = FILE_NAME + '.in'
OUT_FILE = FILE_NAME + '.out'

f = open(IN_FILE, 'r')
src = f.read().split('\n')
f.close()

#maxnum = pow(10, 18)
#ns = []
#for i in range(1, 10000):
#	n = pow(2, i) - 1
#	if maxnum < n:
#		break
#	ns.append(n)
#print ns 
ns = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823, 2147483647, 4294967295, 8589934591, 17179869183, 34359738367, 68719476735, 137438953471, 274877906943, 549755813887, 1099511627775, 2199023255551, 4398046511103, 8796093022207, 17592186044415, 35184372088831, 70368744177663, 140737488355327, 281474976710655, 562949953421311, 1125899906842623, 2251799813685247, 4503599627370495, 9007199254740991, 18014398509481983, 36028797018963967, 72057594037927935, 144115188075855871, 288230376151711743, 576460752303423487]

def f (n):
	return bin(n).count('1')

T = int(src.pop(0))
result = ""
print('############ start #################')
for i in range(T):
	print('############ start %d ###################' % i)
	N = long(src.pop(0).strip())
	m = f(N)
	for n in ns:
		if N < n:
			break
		r = f(n) + f(N - n)
		print '%d(%s) %d(%s) %d' % (n, bin(n), N-n, bin(N-n), r)
		if m < r:
			m = r
				
	result = result + 'Case #%d: %d\n' % (i + 1, m)
	
print('############ end ###################')


f = open(OUT_FILE, 'w')
f.write(result)
f.close()

