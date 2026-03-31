# def is_tree_tile():
# 	x, y = get_pos_x(), get_pos_y()
# 	return (x % 2 == 0 and y % 2 == 0) or ((x + y) % 2 == 0)

# def handle_tile():
# 	harvest()
# 	if is_tree_tile():
# 		plant(Entities.Tree)
# 	else:
# 		plant(Entities.Bush)
		
# def farm_wood(target_value = 100000):
# 	size = 12
# 	set_world_size(size)
# 	while num_items(Items.Wood) < target_value:
# 		for i in range(size):
# 			for j in range(size):
# 				handle_tile()
# 				move(North)
# 			move(East)

def farm_wood(target_value = 100000000):
	clear()
	set_world_size(8)
	MOVES = (North,North,North,North,East)
	EVENODD = (True, False, True, False, True, False, True, False, True, False)
	companions = {}

	def plant_tree():
		global companions
		plant(Entities.Tree)
		companion, pos = get_companion()
		x, y = pos
		while companion == Entities.Carrot or EVENODD[x-y] or (pos in companions and companion != companions[pos]):
			harvest()
			plant(Entities.Tree)
			companion, pos = get_companion()
			x, y = pos
		companions[pos] = companion

	while num_items(Items.Wood) < target_value:
		for dir in MOVES:
			# Tree
			if can_harvest():
				harvest()
				plant_tree()
				if not get_water():
					use_item(Items.Water)
			else:
				if use_item(Items.Fertilizer):
					use_item(Items.Weird_Substance)
					if can_harvest():
						harvest()
						plant_tree()
						if not get_water():
							use_item(Items.Water)
				else:
					companion, pos = get_companion()
					companions[pos] = companion
			move(dir)

			# Companion
			coords = (get_pos_x(), get_pos_y())
			if coords in companions:
				comp = companions.pop(coords)
				entity_type = get_entity_type()
				if entity_type != comp:
					if entity_type != Entities.Grass:
						harvest()
					if comp != Entities.Grass:
						plant(comp)
			move(North)

