_target_value = 1000000
def calculate_pair_steps(world_size):
	return ((world_size - 6) // 2 + 2)

def try_move(direction):
	return move(direction)

def move_home():
	while get_pos_x() != 0:
		try_move(West)
	while get_pos_y() != 0:
		try_move(South)

def return_and_reset():
	change_hat(Hats.Straw_Hat)
	move_home()
	clear()
	change_hat(Hats.Dinosaur_Hat)
	global _target_value
	perform_dino_pattern(_target_value)

def repeat_move(direction, steps):
	for _ in range(steps):
		if not try_move(direction):
			return_and_reset()
			return False
	return True

def perform_dino_pattern(target_value):
	world_size = get_world_size()
	max_index = world_size - 1

	while num_items(Items.Bone) < target_value:
		if not repeat_move(North, max_index):
			return
		if not repeat_move(East, max_index):
			return
		if not repeat_move(South, 1):
			return

		directions = []
		for _ in range(calculate_pair_steps(world_size)):
			directions.append(West)
			directions.append(East)

		for i in range(0, len(directions), 2):
			dir1 = directions[i]
			if i + 1 < len(directions):
				dir2 = directions[i + 1]
			else:
				dir2 = dir1

			if not repeat_move(dir1, max_index - 1):
				return
			if not repeat_move(South, 1):
				return
			if not repeat_move(dir2, max_index - 1):
				return
			if not repeat_move(South, 1):
				return

		if not repeat_move(West, max_index):
			return

def farm_bone(target_value = 100000):
	global _target_value
	_target_value = target_value
	clear()
	set_world_size(32)
	
	change_hat(Hats.Straw_Hat)
	move_home()
	change_hat(Hats.Dinosaur_Hat)

	while num_items(Items.Bone) < target_value:
		perform_dino_pattern(target_value)
