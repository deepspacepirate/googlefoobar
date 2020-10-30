import math
from collections import defaultdict
from fractions import gcd

class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __sub__(self, p2):
		return Point(self.x-p2.x, self.y-p2.y)

	def __str__(self):
		return "(" + str(int(self.x)) + ", " + str(int(self.y)) +")"

	def __repr__(self):
		return str(self)

	def __hash__(self):
		return hash(str(self))

	def __eq__(self,other):
		return self.x == other.x and self.y == other.y

	def length_square(self):
		return (self.x ** 2) + (self.y ** 2)

	def simplify(self):
		common = abs(gcd(self.x, self.y)) or 1
		self.x /= common
		self.y /= common
		return self

def answer(dimensions, your_position, guard_position, distance):
	dims = Point(dimensions[0], dimensions[1])
	p_captn = Point(your_position[0], your_position[1])
	p_guard = Point(guard_position[0], guard_position[1])
	r_square =  distance ** 2

	min_room_coord = Point(
		math.floor((p_captn.x - distance)/dims.x), 
		math.floor((p_captn.y - distance)/dims.y))

	max_room_coord = Point(
		math.ceil ((p_captn.x + distance)/dims.x), 
		math.ceil ((p_captn.y + distance)/dims.y))

	firing_vectors = defaultdict(set)
	captn_vectors  = defaultdict(set)

	# finding all vectors leading towards either self or target and associated lengths
	for i in range(min_room_coord.x, max_room_coord.x+1):
		for j in range(min_room_coord.y, max_room_coord.y+1):
			if i and j:		# i and j not equal to 0
				guard_mirror_coord = mirror_coords(p_guard, i, j, dims.x, dims.y)
				captn_mirror_coord = mirror_coords(p_captn, i, j, dims.x, dims.y)
				
				firing_vect = guard_mirror_coord - p_captn
				captn_vect  = captn_mirror_coord - p_captn
				
				firing_vect_len = firing_vect.length_square()
				captn_vect_len  = captn_vect.length_square()
				
				if firing_vect_len <= r_square:
					firing_vectors[firing_vect.simplify()].add(firing_vect_len)
				
				if captn_vect_len <= r_square:
					captn_vectors[captn_vect.simplify()].add(captn_vect_len)

	for f in captn_vectors:
		if f in firing_vectors:										# if self is in line of fire
			if min(captn_vectors[f]) < min(firing_vectors[f]):		# determine who is hit first
				firing_vectors.pop(f)

	return len(firing_vectors)

# find new coordinates after mirror tiling the plane with "rooms"
def mirror_coords(real_coord, room_x, room_y, w, h):
	return Point(mc(real_coord.x, room_x, w), mc(real_coord.y, room_y, h))

def mc(real_coord, room, dim):
	m = (-1) if room < 0 else (1)
	if room&1:	
		return m * ( real_coord + dim*(abs(room)-1))
	else:			
		return m * (-real_coord + dim*abs(room))

# -------------------------------------------------------------------------------------------------------------------

dimensions = [3, 2]
captain_position = [1, 1]
badguy_position = [2, 1]
distance = 4
# ouput: 7

dimensions = [42, 59]
captain_position = [34, 44]
badguy_position = [6, 34]
distance = 500

dimensions = [300, 275]
captain_position = [150, 150]
badguy_position = [185, 100]
distance = 500
# ouput: 9

print(answer(dimensions, captain_position, badguy_position, distance))
