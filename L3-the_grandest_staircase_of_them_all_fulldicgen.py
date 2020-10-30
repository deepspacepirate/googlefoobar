# uses self similar property of generating function for distinct partitons Q(n)
# time complexity O(n^2)
# space complexity O(n)

# initializes polynomial for n=3
soln = [1, 1, 1, 2, 1, 1, 1]
solnlen = len(soln)

# create space for polynomial coefficients with degree up to n
# higher powers are irrelevant and not calculated or stored
n = 201
soln += [0] * (n-solnlen+2)
solnlen = len(soln)

# multiply soln * (1 + x^i), store coefficients
for i in range(4, n+1):
	degree = int( i*(i+1)/2 )
	indexLastTerm = min(degree+1, solnlen)

	# add parent to parent shifted right by i
	parent = soln[:]
	for j in range (i, indexLastTerm):
		soln[j] = parent[j] + parent[j - i]

dic = soln[0:n]

def answer(n):
	return dic[n] - 1