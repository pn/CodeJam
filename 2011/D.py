#!/usr/bin/env python
for case in xrange(1, int(raw_input())+1):
	N = int(raw_input())
	a = map(int, raw_input().split())
	b = sorted(a)
	num_unsorted = 0.0
	for i in xrange(len(a)):
		if a[i] != b[i]:
			num_unsorted += 1

	print("Case #%d: %f" % (case, num_unsorted))
