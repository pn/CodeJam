#!/usr/bin/env python

for case in xrange(1, int(raw_input())+1):
	N = int(raw_input())
	numbers = []
	for i in xrange(N):
		numbers.append(float(raw_input()))
	print("Case #%d:\n%s" % (case, '\n'.join([str(x) for x in numbers])))
