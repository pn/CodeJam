#!/usr/bin/env python
from sys import stdin
def profit(money, buy, sell):
	shares = money / buy
	return shares * (sell - buy)
N = int(stdin.readline())
for case in range(1, N+1):
	result = 0
	M = int(stdin.readline())
	P = [int(x) for x in stdin.readline().rstrip().split(' ')]
	Pi = sorted([(P[i], i) for i in xrange(len(P)-1)], key=lambda item: item[0])
	for b, i in Pi:
		s, j = sorted([(P[k], k) for k in xrange(i+1, len(P))], key=lambda item: item[0], reverse=True)[0]
		p = profit(M, b, s)
		if p > result:
			result, B, S, I, J = p, b, s, i, j
	if(result > 0):
		print "Case #%d: %d %d %d" % (case, I+1, J+1, result)
	else:
		print "Case #%d: IMPOSSIBLE" % (case, )


