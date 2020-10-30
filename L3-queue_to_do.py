# only slight increase in benchmark times after 1000
MAX_XOR_LEN = 500

def answer(start, length):
	xor_list1 = [xor_range(start + i*length, start + (length-1)*(i+1)) for i in range(length) ]
	
	if length < MAX_XOR_LEN:
		return reduce(xor, xor_list1)
		
	xor_list1a = list_slice(xor_list1, 4)
	
	xor_list2 = [0]*len(xor_list1a)
	shift0 = ((2+(start&1))+(length&3))&3
	shift1 = (shift0+1)&3
	shift2 = (shift0+2)&3
	shift3 = (shift0+3)&3


	xor_list2[shift0] = xor_list1a[shift0][0] if len(xor_list1a[shift0])&1 else 0
	xor_list2[shift2] = xor_list1a[shift2][0] if len(xor_list1a[shift2])&1 else 0
	xor_list2[shift1] = xor_reduce_list(xor_list1a[shift1])
	xor_list2[shift3] = xor_reduce_list(xor_list1a[shift3])

	return reduce(xor, xor_list2)
	
def xor0(x):
	return [x, 1, x+1, 0][x&3]

def xor_range(a, b):
	return xor0(b) ^ xor0(a-1)

def xor_reduce_list(a):
	if len(a) < MAX_XOR_LEN:
		return reduce(xor, a)
	else:
		sublist = list_slice(a, 4)
		xord_sublist = [reduce(xor, sub) for sub in sublist]
		return xor_reduce_list(xord_sublist)

def list_slice(L1, step):
	return [L1[i::step] for i in range(step)]

# ---------------------------------------------------------------------------------------

import statistics
import time

n = 200
for j in range(100, 1000, 100):
	
	MAX_XOR_LEN = j
	times = []
	
	for i in range(n):
		t0 = time.time()
		answer(2000, 44000)
		t1 = time.time()
		times.append(t1-t0)
		
	print(j, sum(times)/n, '+/-', statistics.stdev(times))

