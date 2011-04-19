#!/usr/bin/env python
obstacles = ['R','W','T']
for case in xrange(1, int(raw_input())+1):
	field = []
	[L, W] = [int(x) for x in raw_input().split(' ')]
	for i in range(W):
		field.append(map(lambda x:x in obstacles , raw_input().rstrip()))
	max_area = 0
	for i in xrange(W):
		for j in xrange(L):
			max_w = W-i
			max_l = L-j
			if max_w * max_l <= max_area:
				continue
			for w in xrange(1, max_w+1):
				try:
					first_obstacle = field[i+w-1][j:j+max_l].index(True)
				except ValueError:
					first_obstacle = max_l
					cur_area = w * max_l
					if cur_area > max_area:
						max_area = cur_area
				if first_obstacle > 0:
					max_l = first_obstacle
				else:
					break
	print("Case #%d: %d" % (case, max_area))
