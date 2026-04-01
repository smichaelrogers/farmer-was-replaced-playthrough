from movement import *

def repair_pumpkins():
	size = get_world_size()
	drone_idx = num_drones()
	for _ in range(drone_idx - 2):
		move(East)
	
	while True:
		for i in range(size):
			for j in range(size):
				while get_entity_type() != Entities.Pumpkin or not can_harvest():
					if get_ground_type() != Grounds.Soil:
						till()
					plant(Entities.Pumpkin)
					if get_water() < 0.4:
						use_item(Items.Water)
				move(North)
			move(East)

def farm_pumpkin(target_value = 100000):
	# set_execution_speed(0.5)
	clear()
	set_world_size(32)
	handle = spawn_drone(repair_pumpkins)
	while handle != None:
		do_a_flip()
		handle = spawn_drone(repair_pumpkins)
	
	while num_items(Items.Pumpkin) < target_value:
		move_to(0, 0)
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
