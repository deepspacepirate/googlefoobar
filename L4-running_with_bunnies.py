def answer(times, time_limit):




# test cases

times = [
	[0,	1,	1,	1,	1],
	[1,	0,	1,	1,	1],
	[1,	1,	0,	1,	1],
	[1,	1,	1,	0,	1],
	[1,	1,	1,	1,	0]
]
time_limit = 3
# Output: [0, 1]

times = [
	[0,	2,	2,	2,	-1],
	[9,	0,	2,	2,	-1],
	[9,	3,	0,	2,	-1],
	[9,	3,	2,	0,	-1],
	[9,	3,	2,	2,	0]
]
time_limit = 1
# Output: [1, 2]

times = [
	[0,	2,	2,	2,	-1],
	[9,	0,	2,	2,	-1],
	[9,	3,	0,	2,	-1],
	[9,	3,	2,	0,	-1],
	[9,	-3,	2,	2,	0]
]
time_limit = 1
# Output: [0, 1, 2]

print(answer(times, time_limit))