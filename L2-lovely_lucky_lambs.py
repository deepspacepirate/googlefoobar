# sum of first n fib numbers is F(n+2) - 1
# sum of first n pows of 2 is 2^(x-1) - 1

def answer(total_lambs):
	return fib(total_lambs) - doub(total_lambs)

def fib(sum):
	n = 4
	f = [2, 3, 5]
	while f[1] <= sum+1:
		f[0], f[1], f[2] = f[1], f[2], f[1]+f[2]
		n += 1
	return n-3

def doub(sum):
	return (sum+1).bit_length() - 1

print(answer(143))
