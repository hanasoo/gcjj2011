# -*- coding: utf-8 -*-

FILE_NAME = 'data'
FILE_NAME = 'C-small-attempt3'
#FILE_NAME = 'C-large'
IN_FILE = FILE_NAME + '.in'
OUT_FILE = FILE_NAME + '.out'

def mycmp(x, y):
	if len(x) == len(y):
		if x.count('*') == y.count('*'):
			return cmp(x, y)
		else:
			return cmp(x.count('*'), y.count('*'))
	else:
		return cmp(len(x), len(y))

def search(A, B, n):
	ast = ['*%s*' % A[k:k+n] for k in range(len(A) + 1 - n)]
	ast[0] = ast[0][1:]
	ast[len(ast)-1] = ast[len(ast)-1][:len(ast[len(ast)-1])-1]
	ast = set(ast)
	
	bst = ['*%s*' % B[k:k+n] for k in range(len(B) + 1 - n)]
	bst[0] = bst[0][1:]
	bst[len(bst)-1] = bst[len(bst)-1][:len(bst[len(bst)-1])-1]
	bst = set(bst)
	
	diff = list(ast.difference(bst))
	if 0 < len(diff):
		print diff
		diff.sort(cmp=mycmp)
		print diff
		return diff.pop(0)
	else:
		return False

f = open(IN_FILE, 'r')
src = f.read().split('\n')
f.close()

T = int(src.pop(0))

result = ""
print('############ start #################')
for i in range(T):
	print('############ try %d ###################' % i)
	A = src.pop(0).strip()
	B = src.pop(0).strip()
	
	L = min(len(A), len(B))
	test = []
	for j in range(1, L+1):
		dst = search(A, B, j)
		if dst:
			test.append(dst)
			test.sort(mycmp)
			if len(test) == 3:
				break
	result = result + 'Case #%d: %s\n' % (i + 1, test.pop(0))
	
print('############ end ###################')


f = open(OUT_FILE, 'w')
f.write(result)
f.close()


