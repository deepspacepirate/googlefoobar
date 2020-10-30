def answer(l, t):
	n = len(l)
	for di in range(n):
		for i in range(0, n-di):
			if t == sum(l[i:i+di]):
				return [i, i+di-1]

	return [-1, -1]

l1 = [4, 3, 10, 2, 8]
t1 = 12

l2 = [1, 2, 3, 4]
t2 = 15

print(answer(l1, t1))
print(answer(l2, t2))

