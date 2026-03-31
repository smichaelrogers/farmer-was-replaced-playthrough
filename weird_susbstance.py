from movement import move_to

def farm_weird_substance(target_value = 100000):
	set_world_size(8)
	clear()
	move_to(4,4)
	till()
	use_item(Items.Water)
	use_item(Items.Water)
	use_item(Items.Water)

	# spam trees
	while True:
		use_item(Items.Water)
		for i in range(888): # get_water <= 0.78
			plant(Entities.Tree)
			if Entities.Grass in get_companion():
				use_item(Items.Fertilizer)
			harvest()

	# while num_items(Items.Weird_Substance) < target_value:
	# 	if can_harvest():
	# 		harvest()
	# 	if get_ground_type() != Grounds.Grassland:
	# 		clear()
	# 	else:
	# 		if get_water() < 0.05:
	# 			use_item(Items.Water)
	# 		use_item(Items.Fertilizer)
	# 	move(North)
	# 	if can_harvest():
	# 		harvest()
	# 	if get_ground_type() != Grounds.Grassland:
	# 		clear()
	# 	else:
	# 		if get_water() < 0.05:
	# 			use_item(Items.Water)
	# 		use_item(Items.Fertilizer)
	# 	move(South)