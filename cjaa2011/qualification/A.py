#!/usr/bin/env python
from sys import stdin
N = int(stdin.readline())
case = 1
for i in range(N):
	strings = {'R':[], 'B':[]}
	S = stdin.readline().rstrip()
	l = stdin.readline().rstrip().split(' ')
	for string in l:
		strings[string[-1:]].append(int(string[:-1]))
	lenR, lenB = len(strings['R']), len(strings['B'])
	num = min(lenR, lenB)
	print "Case #%d: %d" % (case, sum(sorted(strings['R'])[lenR-num:]) + sum(sorted(strings['B'])[lenB-num:]) - num * 2)
	case += 1
