#!/usr/bin/env python
#http://code.google.com/codejam/contest/dashboard?c=842485#s=p2

class Message:
	def __init__(self, P, T):
		self.P = P
		self.T = T
	def distance(self, M):
		seconds = abs(self.T - M.T)
		l = abs(self.P - M.P)
		if l - seconds > 0:
			return float(l - seconds) / 2
		return 0

for case in xrange(1, int(raw_input())+1):
	N = int(raw_input())
	messages = []
	for message in xrange(N):
		[P, T] = [int(x) for x in raw_input().split(' ')]
		messages.append(Message(P, T))
	result = 0
	for mi1 in xrange(len(messages)):
		m1 = messages[mi1]
		for m2 in messages[mi1 + 1:]:
			d = m1.distance(m2)
			if d > result:
				result = d
	print "Case #%s: %f" % (case, result)
