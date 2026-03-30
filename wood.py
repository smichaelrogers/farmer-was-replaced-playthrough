def is_tree_tile():
	x, y = get_pos_x(), get_pos_y()
	return (x % 2 == 0 and y % 2 == 0) or ((x + y) % 2 == 0)

def handle_tile():
	harvest()
	if is_tree_tile():
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)
		
def farm_wood(target_value = 100000):
	size = 12
	set_world_size(size)
	while num_items(Items.Wood) < target_value:
		for i in range(size):
			for j in range(size):
				handle_tile()
				move(North)
			move(East)

