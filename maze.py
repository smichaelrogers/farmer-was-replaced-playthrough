RIGHT = {North: East, East: South, South: West, West: North}
LEFT = {North: West, East: North, South: East, West: South}

def farm_gold(target_value = 100000):
	# clear()
	# set_world_size(5)
	# ws = get_world_size()
	# substance = ws * 2**(num_unlocked(Unlocks.Mazes)-1)
	# goal = 9863168
	# rr = range(ws)

	# def drone_search():
	# 	while num_items(Items.Gold) < goal:
	# 		while use_item(Items.Weird_Substance, substance):
	# 			continue
	# 		if get_entity_type() == Entities.Treasure:
	# 			if not use_item(Items.Weird_Substance, substance):
	# 				harvest()
	# 				plant(Entities.Bush)
	# 				use_item(Items.Weird_Substance,substance)


	# for i in rr:
	# 	for j in rr:
	# 		spawn_drone(drone_search)
	# 		move(North)
	# 	move(East)
	# plant(Entities.Bush)
	# use_item(Items.Weird_Substance,substance)
	clear()
	set_world_size(32)
	while num_items(Items.Gold) < target_value:
		AMOUNT = get_world_size() * num_unlocked(Unlocks.Mazes)
		dir=North
		clear()

		# Generate the maze
		plant(Entities.Bush)
		use_item(Items.Weird_Substance, AMOUNT)

		# Follow the left-hand rule until treasure is found
		while get_entity_type() != Entities.Treasure:
			if move(dir):
				# If the move was successful turn left
				dir = RIGHT[dir]
			else:
				# If the move was unsuccessful turn right
				dir = LEFT[dir]
		harvest()