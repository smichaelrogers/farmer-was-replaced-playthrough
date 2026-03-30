def handle_pumpkin_tile():
	if can_harvest():
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() != Entities.Pumpkin:
		plant(Entities.Pumpkin)
		return
	plant(Entities.Pumpkin)

def farm_pumpkin(target_value = 100000):
	while num_items(Items.Carrot) < target_value:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				handle_pumpkin_tile()
				move(North)
			move(East)