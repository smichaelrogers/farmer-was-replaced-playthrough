from movement import *

def repair_pumpkins():
	size = get_world_size()
	drone_idx = num_drones()
	if drone_idx < 5 and drone_idx % 2 == 0:
		move(East)
		while True:
			for i in range(size):
				for j in range(size):
					if get_entity_type() == Entities.Dead_Pumpkin:
						plant(Entities.Pumpkin)
						if get_water() < 0.4:
							use_item(Items.Water)
					move(East)
					move(East)
				move(North)
	elif drone_idx < 5:
		while True:
			for i in range(size):
				for j in range(size):
					if get_entity_type() == Entities.Dead_Pumpkin:
						plant(Entities.Pumpkin)
						if get_water() < 0.4:
							use_item(Items.Water)
					move(East)
					move(East)
				move(North)
	elif drone_idx > 4 and drone_idx % 2 == 0:
		move(North)
		while True:
			for i in range(size):
				for j in range(size):
					if get_entity_type() == Entities.Dead_Pumpkin:
						plant(Entities.Pumpkin)
						if get_water() < 0.4:
							use_item(Items.Water)
					move(North)
					move(North)
				move(East)
	else:
		while True:
			for i in range(size):
				for j in range(size):
					if get_entity_type() == Entities.Dead_Pumpkin:
						plant(Entities.Pumpkin)
						if get_water() < 0.4:
							use_item(Items.Water)
					move(North)
					move(North)
				move(East)

def farm_pumpkin(target_value = 100000):
	clear()
	set_world_size(16)
	NUM_HELPER_DRONES = 7
	for i in range(NUM_HELPER_DRONES):
		spawn_drone(repair_pumpkins)
		do_a_flip()
		do_a_flip()
		do_a_flip()
	
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
