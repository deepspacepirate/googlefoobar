def answer(pegs):
	n = len(pegs)
	if		n <= 1:			return [-1, -1]

	# q = (p1-p0) - (p2-p1) + (p3-p2) ...
	pegDistance = [(pegs[i] - pegs[i-1]) for i in range(1, n)]
	q = sum((-1)**(i) * pegDistance[i] for i in range(n-1))

	# specific case of gaussian elimination
	r = [sum((-1)**(j-i) * pegDistance[j] for j in range(i, n-1)) for i in range(n-1)] + [q]
	if n % 2 == 1:	r[:] = [  r[i] + (-1)**(i) * q for i in range(n)]
	else:			r[:] = [3*r[i] - (-1)**(i) * q for i in range(n)]

	negs = sum(1 for ri in r if ri < 0)

	if 		negs > 0:		return [-1, -1]			# negative gear radius
	elif	n % 2 == 1:		return [r[0], 1]		# n is odd
	elif	r[0] % 3 == 0:	return [r[0]/3, 1]		# n is even
	else:					return [r[0], 3]		# n is even

p1 = [4, 30, 50]
p2 = [4, 17, 50]
print(answer(p2))
