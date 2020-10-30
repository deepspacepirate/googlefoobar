import itertools
import math
from operator import mul
from functools import reduce
from collections import Counter

def answer(m, n, s):
	fixed_states = 0

	for summands_row in partition_generator(m):
		for summands_col in partition_generator(n):

			ncr_row = ncr_list(summands_row)
			ncr_col = ncr_list(summands_col)

			der_row = derangement_list(summands_row)
			der_col = derangement_list(summands_col)

			df = df_calculator(summands_row, summands_col)
			matrix_states = big_power(s, df)

			product = ncr_row * ncr_col * der_row * der_col * matrix_states
			fixed_states += product

			# print(summands_row, summands_col)
			# print('df =', df)
			# print(product, '=', ncr_row, ncr_col, der_row, der_col, matrix_states, '\n')

	return fixed_states // (math.factorial(m) * math.factorial(n))


# degrees of freedom per submatrix
def df_calculator(summands_row, summands_col):
	df = 0
	for (m, n) in itertools.product(summands_row, summands_col):
		df += math.gcd(m,n)
	return df

# how many different ways to select this combination of summands
def ncr_list(summands):
	n 		= sum(summands)
	counts 	= Counter(summands)

	if counts[1] == n:
		return 1
	
	numer = reduce(mul, range(counts[1]+1, n+1))
	perms = reduce(mul, [math.factorial(counts[s]) for s in counts if s!=1])
	denom = reduce(mul, [math.factorial(s) for s in summands if s!= 1]) * perms
	return numer // denom

# number of complete derangements without subcycles
def derangement_list(summands):
	return reduce(mul, [math.factorial(b-1) for b in summands])

# credit to: http://jeromekelleher.net/generating-integer-partitions.html
def partition_generator(n):
	a = [0 for i in range(n + 1)]
	k = 1
	y = n - 1
	while k != 0:
		x = a[k - 1] + 1
		k -= 1
		while 2 * x <= y:
			a[k] = x
			y -= x
			k += 1
		l = k + 1
		while x <= y:
			a[k] = x
			a[l] = y
			yield a[:k + 2]
			x += 1
			y -= 1
		a[k] = x + y
		y = x + y - 1
		yield a[:k + 1]

def big_power(base, power):
	result = 1
	while power > 0:
		if power&1:		# if power is odd
			result = (result * base)
		power >>= 1
		base = base * base
	return result

print(answer(7, 7, 20))

# correct answers
# (2, 2, 2) - 7
# (2, 3, 4) - 430
# (3, 3, 3) - 738
# (3, 3, 4) - 8240
# (3, 3, 5) - 57675
# (2, 5, 3) - 678
# (4, 4, 4) - 7880456
# (4, 4, 5) - 270656150
# (5, 5, 5) - 20834113243925
# (3, 5, 20) - 45568090499534008
# (4, 4, 20) - 1137863754106723400
# (5, 5, 20) - 23301834615661488487765745000
# (6, 6, 20) - 132560781153101038829213988789736592649360
# (7, 7, 20) - 221619886894198821201872678876163305792210161226545392840
# (8, 8, 20) - 113469378614817897312718329989374518983724697432844009920312263602471667640