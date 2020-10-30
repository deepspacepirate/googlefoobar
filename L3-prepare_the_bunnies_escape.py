# O(m*n) where m and n are dimensions of the matrix

import math
import itertools
from collections import defaultdict

def answer(maze):
	h, w = len(maze), len(maze[0])

	distances_to_Start = wavefront_expansion(maze, (0, 0))
	distances_to_End   = wavefront_expansion(maze, (h-1, w-1))
	tentative_path_len = distances_to_End[(0,0)]

	if tentative_path_len == w + h - 1:
		return tentative_path_len

	for x,y in breakable_walls(maze):
		adjNodes = get_neighbors(maze, h, w, x, y)

		to_node_distances = [distances_to_Start[node] for node in adjNodes]
		fr_node_distances = [distances_to_End  [node] for node in adjNodes]

		shortest_path = min([to + fr + 1 for to,fr in itertools.product(to_node_distances, fr_node_distances)])
		tentative_path_len = min(tentative_path_len, shortest_path)

	return tentative_path_len

# Dijkstra's algorithm
def wavefront_expansion(maze, start):
	h, w = len(maze), len(maze[0])

	scores = defaultdict(lambda:w*h)		# distance from start
	scores[start] = 1

	open_set = {start}		# discovered nodes, not evaluated
	closed_set = set()		# evaluated nodes

	while open_set:
		to_add = set()

		for current in open_set:
			closed_set.add(current)
			
			for neighbor in get_neighbors(maze, h, w, current[0], current[1]):
				if neighbor in closed_set:					# already looked at
					continue
				if neighbor not in open_set:				# newly discovered
					to_add.add(neighbor)
				if scores[neighbor] > scores[current] + 1:	# update distance from start for nodes in open_set
					scores[neighbor] = scores[current] + 1
		
		open_set = to_add

	return scores

def breakable_walls(maze):
	h, w = len(maze), len(maze[0])
	for i in range(h):
		for j in range(w):
			if maze[i][j] == 1:
				adjNodes = get_neighbors(maze, h, w, i, j)
				
				if len(adjNodes) >= 3:
					yield (i, j)

				# only break if not a corner
				elif len(adjNodes) == 2:		
					dx = round_away_from_zero((adjNodes[0][0] + adjNodes[1][0])/2 - i)
					dy = round_away_from_zero((adjNodes[0][1] + adjNodes[1][1])/2 - j)

					if maze[i+dx][j+dy] == 1:
						yield (i, j)

def get_neighbors(maze, h, w, i, j):
	h, w = len(maze), len(maze[0])
	moveset = [(-1, 0), (0, 1), (1, 0), (0, -1)]

	positions = [
		(i+di, j+dj) for (di,dj) in moveset 		# next available coordinates
		if  (0 <= (i+di) < h)						# that don't hit the boundary
		and (0 <= (j+dj) < w)
		and (maze[i+di][j+dj] != 1)					# or the walls
	]

	return positions

def round_away_from_zero(x):
	return math.floor(x) if x < 0 else math.ceil(x)

# 7
maze1 = [
	[0, 1, 1, 0], 
	[0, 0, 0, 1], 
	[1, 1, 0, 0], 
	[1, 1, 1, 0]]


# 11
maze2 = [
	[0, 0, 0, 0, 0, 0],
	[1, 1, 1, 1, 1, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 1, 1, 0, 0, 1],
	[0, 1, 1, 0, 0, 1],
	[0, 0, 0, 0, 0, 0]]

print(answer(maze2))
