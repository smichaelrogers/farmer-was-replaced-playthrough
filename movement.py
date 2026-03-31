def move_to_start():
	for _ in range(get_pos_y()):
		move(South)
	for _ in range(get_pos_x()):
		move(West)


def generate_moves(
		n = get_world_size()**2,
		world_size = get_world_size(),
		pos_x = 0,
		pos_y = 0
	):
	moves = []
	if n > world_size**2:
		world_moves = generate_moves(world_size**2, world_size, pos_x, pos_y)
		for i in range(n // world_size**2):
			moves += world_moves
		n %= world_size**2

	for i in range(n):
		if pos_x % world_size == pos_y % world_size:
			pos_x -= 1
			moves.append(West)
		else:
			pos_y += 1
			moves.append(North)
	return moves

MOVES = generate_moves()

def move_to(goal_x, goal_y, current_x = get_pos_x(), current_y = get_pos_y(), ws = get_world_size()):
	hws = ws // 2
	# Calculate the shortest x direction
	dx = (goal_x - current_x + hws) % ws - hws
	# Calculate the shortest y direction
	dy = (goal_y - current_y + hws) % ws - hws

	# Move in x direction
	for _ in range(dx):
		move(East)
	for _ in range(-dx):
		move(West)

	# Move in y direction
	for _ in range(dy):
		move(North)
	for _ in range(-dy):
		move(South)


def move_to_pos(goal_pos, current_pos, ws = get_world_size()):
	hws = ws // 2
	goal_x, goal_y = goal_pos
	start_x, start_y = current_pos

	dx = (goal_x - start_x + hws) % ws - hws
	dy = (goal_y - start_y + hws) % ws - hws

	for i in range(dx):
		move(East)
	for i in range(-dx):
		move(West)
	for i in range(dy):
		move(North)
	for i in range(-dy):
		move(South)
