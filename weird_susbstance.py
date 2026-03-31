from movement import move_to

def farm_weird_substance(target_value = 100000):
	clear()
	set_world_size(8)
	move_to(4,4)
	till()
	use_item(Items.Water)
	use_item(Items.Water)
	use_item(Items.Water)

	while num_items(Items.Weird_Substance) < target_value:
		use_item(Items.Water)
		for i in range(888): # get_water <= 0.78
			plant(Entities.Tree)
			if Entities.Grass in get_companion():
				use_item(Items.Fertilizer)
			harvest()