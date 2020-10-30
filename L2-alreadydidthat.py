def answer(n, b):
	ids = []
	z = zCalc(n, b)

	while (z not in ids):
		ids.append(z)
		z = zCalc(z, b)

	return len(ids) - ids.index(z)

def zCalc(n, b):
	# get x and y
	nStr = str(n)
	k = len(nStr)
	y = sorted([int(i) for i in nStr])
	x = y[::-1]
	
	# base subtraction
	z = [x[i] - y[i] for i in range(k)]
	for i in range(k-1, 0, -1):
		if (z[i] < 0):  
			z[i] += b
			z[i-1] -= 1
			
		elif (z[i] >= b):
			z[i] -= b
			z[i-1] += 1

	return int(''.join(map(str, z)))
	
print(answer(1211, 10))
print(answer(210022, 3))
