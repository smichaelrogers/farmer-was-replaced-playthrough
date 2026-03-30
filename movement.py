def move_to_start():
	for i in range(get_pos_y()):
		move(South)
	for i in range(get_pos_x()):
		move(West)

def move_to(to_x, to_y):
	x, y = get_pos_x(), get_pos_y()
	while x > to_x:
		move(West)
		x = get_pos_x()
	while x < to_x:
		move(East)
		x = get_pos_x()
	while y > to_y:
		move(South)
		y = get_pos_y()
	while y < to_y:
		move(North)
		y = get_pos_y()