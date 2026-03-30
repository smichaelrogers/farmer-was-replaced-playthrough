def farm_weird_substance(target_value = 100000):
	while num_items(Items.Weird_Substance) < target_value:
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Grassland:
			clear()
		else:
			if get_water() < 0.05:
				use_item(Items.Water)
			use_item(Items.Fertilizer)
		move(North)
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Grassland:
			clear()
		else:
			if get_water() < 0.05:
				use_item(Items.Water)
			use_item(Items.Fertilizer)
		move(South)