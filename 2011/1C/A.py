#!/usr/bin/env python
for case in xrange(1, int(raw_input())+1):
	result = "Impossible"
	t = []
	R, C = map(int, raw_input().strip().split())
	for i in xrange(R):
		t.append(list(raw_input().strip()))
	for i in xrange(R-1):
		for j in xrange(C-1):
			if t[i][j] == '#' and t[i][j+1] =='#' and t[i+1][j] == '#' and t[i+1][j+1] == '#':
				t[i][j] = '/'
				t[i+1][j] = '\\'
				t[i][j+1] = '\\'
				t[i+1][j+1] = '/'
	bad = False
	for i in xrange(R):
		if '#' in t[i]:
			bad = True
	if not bad:
		result = '\n'.join([''.join(x) for x in t])
	print("Case #%d: \n%s" % (case, result))
