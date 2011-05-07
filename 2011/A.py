#!/usr/bin/env python
for case in xrange(1, int(raw_input())+1):
	t = raw_input().split()
	N = t[0]
	t = t[1:]
	R = t[0::2]
	P = map(int, t[1::2])
	result = 0
	position = {'O': 1, 'B': 1}
	other = {'O': 'B', 'B': 'O'}
	moved = {'O': 0, 'B': 0}
	previously = ''
	for ri in xrange(len(R)):
		r = R[ri]
		p = P[ri]
		if previously != r:
			moved[r] = 0
		distance = abs(position[r] - p)
		movednow = distance + 1
		if distance > 0 and moved[other[r]] > 0:
			movednow -= min(moved[other[r]], distance)
		moved[other[r]] = 0
		result += movednow
		moved[r] += movednow
		position[r] = p
		previously = r

	print("Case #%d: %d" % (case, result))
