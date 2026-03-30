def is_even(x):
	return x % 2 == 0
def is_odd(x):
	return x % 2 == 1
	
def goto(x, y):
	y_distance = get_pos_y() - y
	x_distance = get_pos_x() - x
	half_size = get_world_size() / 2
	while get_pos_y() != y:
		if y_distance >= half_size or (- half_size <= y_distance and y_distance < 0):
			move(North)
		else:
			move(South)
	while get_pos_x() != x:
		if x_distance >= half_size or (- half_size <= x_distance and x_distance < 0):
			move(East)
		else:
			move(West)
			
def backtrack(route, x, y):
	if x > route[0]:
		move(West)
	elif x < route[0]:
		move(East)
	elif y > route[1]:
		move(South)
	elif y < route[1]:
		move(North)


def get_field(size, element):
	x_ary = []
	for x in range(size):
		y_ary = []
		for y in range(size):
			y_ary.append(element)
		x_ary.append(y_ary)
	return x_ary