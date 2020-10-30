# absorbing markov chains
# all matrices in the form M[i][j] where i is column and j is row

def answer(matrix):
	n = len(matrix)
	sums = [sum(matrix[i]) for i in range(n)]
	sigma = lcm_list(sums)

	# dimensions of submatrix A
	nA = len([x for x in sums if x != 0])
	
	# scales each nonzero col up
	for i in range(nA):
		multiplier = sigma / sums[i]
		for j in range(n):
			matrix[i][j] *= multiplier

	A = [matrix[i][:nA] for i in range(nA)]
	B = [matrix[i][nA:] for i in range(nA)]

	# B * (sI-A)^(-1)
	# only interested in first col because fuel always starts in s0
	ans = matrixMult(B, matrixInvScaled(matrixSub(eye(nA, sigma), A)))[0]

	return cleanup(ans)

# scales down and appends denominator
def cleanup(a):
	gcf = gcd_list(a)
	temp = [x/gcf for x in a]
	temp.extend([sum(temp)])
	return temp

# returns a scaled version of the inverse s.t. there are no fractions
def matrixInvScaled(a):
	m = len(a)
	inv = []

	if m == 1:
		inv = [1]

	if m == 2:
		inv = [[a[1][1], -a[0][1]], [-a[1][0], a[0][0]]]

	# gauss-jordan reduction
	else:
		a.extend(eye(m, 1))
		n = len(a)

		# change from col,row to row, col notation
		c = [list(row) for row in zip(*a)]
		
		for p in range(m): # select pivot col

			# swap rows if pivot equals to zero
			if c[p][p] == 0:
				rows_with_nonzero_pivot = [k for k in range(p, m) if c[k][p] != 0]
				selected_row = rows_with_nonzero_pivot[0]
				c[p], c[selected_row] = c[selected_row], c[p]

			# make pivot positive
			if c[p][p] < 0:
				c[p] = [x*-1 for x in c[p]]

			# row addition to clear col
			for i in range(m):	
				if i != p and c[i][p] != 0:
					a = c[p][p]
					b = c[i][p]
					l = abs(lcm(a, b))

					for k in range(n):
						c[i][k] = c[p][k] * l/a - c[i][k] * l/b

		lcm_diag = lcm_list([c[i][i] for i in range(m)])
		for i in range(m):
			first = c[i][i]
			for j in range(i, n):
				c[i][j] *= lcm_diag/first 
		
		inv = [list(col) for col in zip(*c)][m:n]
	
	return inv

def matrixMult(a, b):
	zip_a = list(zip(*a))
	return [[sum(el_a*el_b for el_a, el_b in zip(row_a, col_b)) for row_a in zip_a] for col_b in b]

def matrixSub(a, b):
	cols = len(a)
	rows = len(a[0])
	return [[a[i][j] - b[i][j]for j in range(rows)] for i in range(cols)]	

def eye(n, a):
	r = [[0] * n for i in range(n)]
	for i in range(n):
		r[i][i] = a
	return r

def lcm_list(a):
	mult = a[0]
	for x in a[1:]:
		if x != 0: 
			mult = lcm(mult, x)
	return mult

def lcm(a, b):
	return a * b / gcd(a, b)

def gcd_list(a):
	factr = a[0]
	for x in a[1:]:
		if x != 0:
			factr = gcd(factr, x)
	return factr

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

# ...................................................................................

inData1 = [
	[0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
	[4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
	[0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
	[0,0,0,0,0,0],  # s3 is terminal
	[0,0,0,0,0,0],  # s4 is terminal
	[0,0,0,0,0,0],  # s5 is terminal
]

inData2 = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
inData3 = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

ans = answer(inData3)
print(ans)

