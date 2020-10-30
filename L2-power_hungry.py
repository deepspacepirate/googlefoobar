from functools import reduce
from operator import mul

def answer(xs):
	ans = reduce(mul, [x for x in xs if abs(x) >= 1])
	if ans < 0:
		ans /= max(x for x in xs if x <= -1)
	return str(ans)

list1 = [-2, -3, 4, -5]
list2 = [2, 0, 2, 2, 0]
print(answer(list2))
