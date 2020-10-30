def answer(mStr, fStr):
	m = int(mStr)
	f = int(fStr)
	
	if (f==0 or m==0):
		return "impossible"

	gen = 0
	while True:

		if(m==1 and f==1):
			return str(gen)
		elif (f==m):
			return "impossible"

		if (f > m):
			f, m = m, f
		
		if (m > 2*f):
			curGen = int((m-1)/f)
			gen += curGen
			m -= curGen*f
		else:
			m -= f
			gen += 1
		  
print(answer(41, 183))

# output: 1
print(answer(2, 1))

# output: 4
print(answer(4, 7))

# output: impossible
print(answer(2, 4))
