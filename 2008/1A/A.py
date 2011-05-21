#!/usr/bin/env python
import operator
for case in xrange(1, int(raw_input())+1):
	n = int(raw_input())
	result = 0
	a = map(int, raw_input().split())
	b = map(int, raw_input().split())
	a = sorted(a)
	b = sorted(b, reverse=True)
	result = sum(map(operator.mul,a,b))
	print("Case #%d: %d" % (case, result))

