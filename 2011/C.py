#!/usr/bin/env python
for case in xrange(1, int(raw_input())+1):
	N = int(raw_input())
	C = map(int, raw_input().split())
	s = 0
	for c in C:
		s = s ^ c
	if s:
		answer = 'NO'
	else:
		answer = sum(sorted(C)[1:])

	print("Case #%d: %s" % (case, answer))
