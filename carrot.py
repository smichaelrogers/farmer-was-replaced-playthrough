def handle_carrot_tile():
	if can_harvest():
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Carrot)

def farm_carrot(target_value = 100000):
	while num_items(Items.Carrot) < target_value:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				handle_carrot_tile()
				move(North)
			move(East)