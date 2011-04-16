#!/usr/bin/env python
# http://code.google.com/codejam/contest/dashboard?c=189252#s=p0
import sys

T = int(sys.stdin.readline())
for case in range(1, T+1):
	number = sys.stdin.readline().rstrip()
	digits = {}
	num = 2
	for c in number:
		if c in digits:
			continue
		if not 1 in digits.values():
			digits[c] = 1
		elif not 0 in digits.values():
			digits[c] = 0
		else:
			digits[c] = num
			num += 1
	base = len(digits)
	if base == 1:
		base = 2
	result = 0
	for c in number[:-1]:
		result = (result + digits[c]) * base
	result += digits[number[-1]]
	print("Case #%d: %d" % (case, result))
