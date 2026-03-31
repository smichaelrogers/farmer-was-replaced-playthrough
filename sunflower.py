clear()
set_world_size(8)

def generate_moves(
		n = get_world_size()**2,
		world_size = get_world_size(),
		pos_x = 0,
		pos_y = 0
	):
	moves = []
	if n > world_size**2:
		world_moves = generate_moves(world_size**2, world_size, pos_x, pos_y)
		for i in range(n // world_size**2):
			moves += world_moves
		n %= world_size**2

	for i in range(n):
		if pos_x % world_size == pos_y % world_size:
			pos_x -= 1
			moves.append(West)
		else:
			pos_y += 1
			moves.append(North)
	return moves

MOVES = generate_moves()

def farm_power(target_value = 100000):
	while num_items(Items.Power) < target_value:
		# pre plant
		for direction in MOVES:
			if get_ground_type() == Grounds.Grassland:
				till()
			while measure() != 7:
				harvest()
				plant(Entities.Sunflower)
			move(direction)

		# pre water
		for _ in range(10):
			move(North)
			use_item(Items.Water)
			use_item(Items.Water)
			use_item(Items.Water)
			use_item(Items.Water)

		# main loop
		time = get_time()
		while get_time() - time < 60:
			if get_water() <= 0.78:
				use_item(Items.Water)
			harvest()
			plant(Entities.Sunflower)
			while measure() != 7:
				use_item(Items.Fertilizer)
				use_item(Items.Weird_Substance)
				harvest()
				plant(Entities.Sunflower)
				use_item(Items.Fertilizer)
				use_item(Items.Weird_Substance)
				harvest()
				plant(Entities.Sunflower)
			move(North)

		# post harvest
		for direction in MOVES:
			harvest()
			move(direction)
