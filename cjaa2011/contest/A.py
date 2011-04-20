#!/usr/bin/env python
from operator import itemgetter
max_depth = 50
def check(l, r, n, depth):
	#print 'check', l, r, n, depth
	if depth == max_depth:
		return depth
	t = (r - l)/3
	if n >= l + t:
		if n <= r - t:
			return depth
		else:
			return check(r - t, r, n, depth + 1)
	else:
		return check(l, l + t, n, depth + 1)

for case in xrange(1, int(raw_input())+1):
	N = int(raw_input())
	numbers = []
	for i in xrange(N):
		numbers.append(float(raw_input()))
	result = []
	for number in numbers:
		result.append((check(float(0), float(1), number, 0), number))
	#print [(x, y) for x, y in sorted(result, key=itemgetter(0,1))]
	print("Case #%d:\n%s" % (case, '\n'.join([str(y) for x, y in sorted(result, key=itemgetter(0,1))])))
