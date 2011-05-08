#!/usr/bin/env python
for case in xrange(1, int(raw_input())+1):
	N = int(raw_input())
	C = map(int, raw_input().split())
	s = reduce(lambda x,y: x^y, C)
	answer = 'NO'
	if not s:
		answer = sum(C)-min(C)

	print("Case #%d: %s" % (case, answer))
