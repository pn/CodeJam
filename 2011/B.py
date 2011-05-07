#!/usr/bin/env python
for case in xrange(1, int(raw_input())+1):
	t = raw_input().split()
	C, t = int(t[0]), t[1:]
	c, t = t[:C], t[C:]
	D, t = int(t[0]), t[1:]
	d, t = t[:D], t[D:]
	N, t = int(t[0]), t[1:]
	n = list(t[0])
	result = []
	for elem in n:
		result.append(elem) #invoke element
		#combine
		while len(result) > 1:
			e1, e2 = result[-1], result[-2]
			combined = False
			for celem in c:
				if e1 in celem[:2] and e2 in celem[:2]:
					if e1 == e2 and celem[:2].replace(e1, ''):
						continue
					result.pop()
					result[-1] = celem[2]
					combined = True
			if not combined:
				break
		#oppose
		if len(result) > 1:
			e = result[-1]
			for delem in d:
				if e in delem:
					o = delem.replace(e, '')
					if o in result:
						result = []
						break

	print("Case #%d: [%s]" % (case, ', '.join(result)))
