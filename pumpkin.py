# from movement import move_to
from movement import MOVES

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


def handle_pumpkin_tile():
	harvest()
	till()
	plant(Entities.Pumpkin)

def farm_pumpkin(target_value = 100000):
	clear()
	move_to(0, 0)
	for dir in MOVES:
		till()
		plant(Entities.Pumpkin)
		move(dir)
	while num_items(Items.Pumpkin) < target_value:
		pumpkin_set = list()
		# 1. just plant and move
		for dir in MOVES:
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Pumpkin)
			move(dir)

		# 2. plant and append to dict
		for dir in MOVES:
			if not can_harvest():
				plant(Entities.Pumpkin)
				pumpkin_set.append((get_pos_x(), get_pos_y()))
			move(dir)

		# 3. visit all missing pumpkins until we have enough fertilizer
		current_pos = (get_pos_x(), get_pos_y())
		while len(pumpkin_set) > num_items(Items.Fertilizer)/2+2:
			for pos in list(pumpkin_set):
				move_to_pos(pos, current_pos)
				current_pos = pos
				if can_harvest():
					pumpkin_set.remove(pos)
				else:
					plant(Entities.Pumpkin)
					if get_water() < 0.4:
						use_item(Items.Water)

		# 4. navigate through all remaining pumpkins and force
		for pos in pumpkin_set:
			move_to_pos(pos, current_pos)
			current_pos = pos
			while not can_harvest():
				plant(Entities.Pumpkin)
				use_item(Items.Fertilizer)

		# 5. harvest
		harvest()
