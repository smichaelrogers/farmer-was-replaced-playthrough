RIGHT = {North: East, East: South, South: West, West: North}
LEFT = {North: West, East: North, South: East, West: South}

def farm_gold(target_value = 100000):
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