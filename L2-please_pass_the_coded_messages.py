from itertools import combinations

def answer(l):
	l.sort(reverse=True)

	for i in range(len(l), 0, -1):
		for c in itertools.combinations(l, i):
			if sum(c) % 3 == 0:
				return int(''.join(map(str, c)))

	return 0



