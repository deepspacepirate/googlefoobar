def answer(x, y):
	yAdjusted = y + x - 2
	return yAdjusted * (yAdjusted + 1) / 2 + x

# 	4	|	7	8	9	10
# 	3	|	4	5	6
# 	2	|	2	3
# 	1	|	1
# -----------------------
# 	y/x	|	1	2	3	4

# y shifted up by x-1
# x stays the same

# y' = y + x-1
# x' = x

# (3, 1) -> (3, 3)
# find (y'-1)th triangular number and add x
# yAdjusted = (y'-1) = y + x - 2