#!/usr/bin/env python
for case in xrange(1, int(raw_input())+1):
	N = int(raw_input())
	WP = [0.]*N
	OWPB = []
	OWP = [0.]*N
	OOWP = [0.]*N
	RPI = [0.]*N
	oponents = []
	games = []
	for i in xrange(N):
		games.append(raw_input().strip())
		wins = 0.
		loses = 0.
		oponents.append([])
		for j in xrange(len(games[i])):
			game = games[i][j]
			if game != '.':
				oponents[i].append(j)
			if game == '1':
				wins += 1.
			elif game == '0':
				loses += 1.
		WP[i] = wins/len(oponents[i])
		OWPB.append([])
		for j in xrange(len(games[i])):
			game = games[i][j]
			if game != '.':
				if game == '1':
					OWPB[i].append((wins-1)/(len(oponents[i])-1))
				else:
					OWPB[i].append(wins/(len(oponents[i])-1))
			else:
				OWPB[i].append(WP[i])
	for i in range(N):
		for oponent in range(len(oponents[i])):
			OWP[i] += OWPB[oponents[i][oponent]][i]
		OWP[i] = float(OWP[i]) / len(oponents[i])

	for i in range(N):
		for oponent in range(len(oponents[i])):
			OOWP[i] += OWP[oponents[i][oponent]]
		OOWP[i] = float(OOWP[i]) / len(oponents[i])
	
	for i in xrange(N):
		RPI[i] = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]
	print("Case #%d: " % case)
	for i in RPI:
		print("%.6f" % i)
