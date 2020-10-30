from collections import defaultdict

def answer(nums):
	# generage list of divisors and multiples for each number in nums
	length = len(nums)
	divisors = [set() for i in range(length)]
	multiples = [set() for i in range(length)]

	for i in range(length):
		for j in range(i+1, length):
			if nums[j] % nums[i] == 0:
				divisors[j].add(nums[i])
				multiples[i].add(nums[j])
	
	# remove entries with no divisors or multiples
	for i in reversed(range(length)):
		if not (divisors[i] or multiples[i]):
			del nums[i], divisors[i], multiples[i]
	length = len(nums)

	# dictionary for nums and their indicies 
	dic = dictionary(nums)
	duplicates, single = [], []
	for entry in dic:
		if len(entry) > 1:	duplicates.append(entry)
		else:				single.extend(entry)

	# FINALLY COUNTING THE TRIPLES
	triples = 0

	# for numbers that only show up once
	for i in single:
		triples += len(divisors[i])*len(multiples[i])

	# for numbers that show up >1 time
	for indicies in duplicates:
		combo_dict = defaultdict(set)
		for index in indicies:
			for div in divisors[index]:
				combo_dict[div].update(multiples[index])

		for div in combo_dict:
			triples += len(combo_dict[div])

	return triples

def dictionary(seq):
	tally = defaultdict(list)
	for i,item in enumerate(seq):
		tally[item].append(i)
	return [locs for key,locs in tally.items()]

# ---------------------------------------------------------------------------------------
import statistics
import time

list1 = [1, 2, 1, 1, 2, 4, 2, 3, 1, 4, 5, 6]
list2 = [1, 2, 1, 2, 4, 2, 1, 4, 2, 6, 8]
list3 = [1, 2, 8, 2]
list4 = [3]*2000
list5 = [3]*100 + [12]*100 + [6]*100 + [12]*100 + [24]*100
list6 = []
for i in range(20):
	list6.extend([2 ** i] * 100)

list7 = []
for i in range(1, 1000):
	list7.extend([2 * i])

n = 10
ans = 0
times = []
for i in range(n):
	t0 = time.time()
	ans = answer(list2)
	t1 = time.time()
	times.append(t1-t0)
print('dict')
print(ans, sum(times)/n, '+/-', statistics.stdev(times))

