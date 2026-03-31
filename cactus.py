_moves = None
def update(ws=get_world_size()):
	global _moves
	if ws == 10:
		_moves = (
			(
				(),
				(North,),
				(North, North),
				(North, North, North),
				(North, North, North, North),
				(South, South, South, South, South),
				(South, South, South, South),
				(South, South, South),
				(South, South),
				(South,),
			),
			(
				(East,),
				(East, North),
				(East, North, North),
				(East, North, North, North),
				(East, North, North, North, North),
				(East, South, South, South, South, South),
				(East, South, South, South, South),
				(East, South, South, South),
				(East, South, South),
				(East, South),
			),
			(
				(East, East),
				(East, East, North),
				(East, East, North, North),
				(East, East, North, North, North),
				(East, East, North, North, North, North),
				(East, East, South, South, South, South, South),
				(East, East, South, South, South, South),
				(East, East, South, South, South),
				(East, East, South, South),
				(East, East, South),
			),
			(
				(East, East, East),
				(East, East, East, North),
				(East, East, East, North, North),
				(East, East, East, North, North, North),
				(East, East, East, North, North, North, North),
				(East, East, East, South, South, South, South, South),
				(East, East, East, South, South, South, South),
				(East, East, East, South, South, South),
				(East, East, East, South, South),
				(East, East, East, South),
			),
			(
				(East, East, East, East),
				(East, East, East, East, North),
				(East, East, East, East, North, North),
				(East, East, East, East, North, North, North),
				(East, East, East, East, North, North, North, North),
				(East, East, East, East, South, South, South, South, South),
				(East, East, East, East, South, South, South, South),
				(East, East, East, East, South, South, South),
				(East, East, East, East, South, South),
				(East, East, East, East, South),
			),
			(
				(West, West, West, West, West),
				(West, West, West, West, West, North),
				(West, West, West, West, West, North, North),
				(West, West, West, West, West, North, North, North),
				(West, West, West, West, West, North, North, North, North, ),
				(West, West, West, West, West, South, South, South, South, South),
				(West, West, West, West, West, South, South, South, South),
				(West, West, West, West, West, South, South, South),
				(West, West, West, West, West, South, South),
				(West, West, West, West, West, South),
			),
			(
				(West, West, West, West),
				(West, West, West, West, North),
				(West, West, West, West, North, North),
				(West, West, West, West, North, North, North),
				(West, West, West, West, North, North, North, North),
				(West, West, West, West, South, South, South, South, South),
				(West, West, West, West, South, South, South, South),
				(West, West, West, West, South, South, South),
				(West, West, West, West, South, South),
				(West, West, West, West, South),
			),
			(
				(West, West, West),
				(West, West, West, North),
				(West, West, West, North, North),
				(West, West, West, North, North, North),
				(West, West, West, North, North, North, North),
				(West, West, West, South, South, South, South, South),
				(West, West, West, South, South, South, South),
				(West, West, West, South, South, South),
				(West, West, West, South, South),
				(West, West, West, South),
			),
			(
				(West, West),
				(West, West, North),
				(West, West, North, North),
				(West, West, North, North, North),
				(West, West, North, North, North, North),
				(West, West, South, South, South, South, South),
				(West, West, South, South, South, South),
				(West, West, South, South, South),
				(West, West, South, South),
				(West, West, South),
			),
			(
				(West,),
				(West, North),
				(West, North, North),
				(West, North, North, North),
				(West, North, North, North, North),
				(West, South, South, South, South, South),
				(West, South, South, South, South),
				(West, South, South, South),
				(West, South, South),
				(West, South),
			),
		)
	elif ws == 3:
		_moves = (
			((), (North,), (South,)),
			((East,), (East, North), (East, South)),
			((West,), (West, North), (West, South)),
		)
	elif ws == 4:
		_moves = (
			((), (North,), (South, South), (South,)),
			((East,), (East, North), (East, South, South), (East, South)),
			(
				(West, West),
				(West, West, North),
				(West, West, South, South),
				(West, West, South),
			),
			((West,), (West, North), (West, South, South), (West, South)),
		)
	elif ws == 5:
		_moves = (
			((), (North,), (North, North), (South, South), (South,)),
			(
				(East,),
				(East, North),
				(East, North, North),
				(East, South, South),
				(East, South),
			),
			(
				(East, East),
				(East, East, North),
				(East, East, North, North),
				(East, East, South, South),
				(East, East, South),
			),
			(
				(West, West),
				(West, West, North),
				(West, West, North, North),
				(West, West, South, South),
				(West, West, South),
			),
			(
				(West,),
				(West, North),
				(West, North, North),
				(West, South, South),
				(West, South),
			),
		)
	elif ws == 6:
		_moves = (
			(
				(),
				(North,),
				(North, North),
				(South, South, South),
				(South, South),
				(South,),
			),
			(
				(East,),
				(East, North),
				(East, North, North),
				(East, South, South, South),
				(East, South, South),
				(East, South),
			),
			(
				(East, East),
				(East, East, North),
				(East, East, North, North),
				(East, East, South, South, South),
				(East, East, South, South),
				(East, East, South),
			),
			(
				(West, West, West),
				(West, West, West, North),
				(West, West, West, North, North),
				(West, West, West, South, South, South),
				(West, West, West, South, South),
				(West, West, West, South),
			),
			(
				(West, West),
				(West, West, North),
				(West, West, North, North),
				(West, West, South, South, South),
				(West, West, South, South),
				(West, West, South),
			),
			(
				(West,),
				(West, North),
				(West, North, North),
				(West, South, South, South),
				(West, South, South),
				(West, South),
			),
		)
	elif ws == 7:
		_moves = (
			(
				(),
				(North,),
				(North, North),
				(North, North, North),
				(South, South, South),
				(South, South),
				(South,),
			),
			(
				(East,),
				(East, North),
				(East, North, North),
				(East, North, North, North),
				(East, South, South, South),
				(East, South, South),
				(East, South),
			),
			(
				(East, East),
				(East, East, North),
				(East, East, North, North),
				(East, East, North, North, North),
				(East, East, South, South, South),
				(East, East, South, South),
				(East, East, South),
			),
			(
				(East, East, East),
				(East, East, East, North),
				(East, East, East, North, North),
				(East, East, East, North, North, North),
				(East, East, East, South, South, South),
				(East, East, East, South, South),
				(East, East, East, South),
			),
			(
				(West, West, West),
				(West, West, West, North),
				(West, West, West, North, North),
				(West, West, West, North, North, North),
				(West, West, West, South, South, South),
				(West, West, West, South, South),
				(West, West, West, South),
			),
			(
				(West, West),
				(West, West, North),
				(West, West, North, North),
				(West, West, North, North, North),
				(West, West, South, South, South),
				(West, West, South, South),
				(West, West, South),
			),
			(
				(West,),
				(West, North),
				(West, North, North),
				(West, North, North, North),
				(West, South, South, South),
				(West, South, South),
				(West, South),
			),
		)
	elif ws == 8:
		_moves = (
			(
				(),
				(North,),
				(North, North),
				(North, North, North),
				(South, South, South, South),
				(South, South, South),
				(South, South),
				(South,),
			),
			(
				(East,),
				(East, North),
				(East, North, North),
				(East, North, North, North),
				(East, South, South, South, South),
				(East, South, South, South),
				(East, South, South),
				(East, South),
			),
			(
				(East, East),
				(East, East, North),
				(East, East, North, North),
				(East, East, North, North, North),
				(East, East, South, South, South, South),
				(East, East, South, South, South),
				(East, East, South, South),
				(East, East, South),
			),
			(
				(East, East, East),
				(East, East, East, North),
				(East, East, East, North, North),
				(East, East, East, North, North, North),
				(East, East, East, South, South, South, South),
				(East, East, East, South, South, South),
				(East, East, East, South, South),
				(East, East, East, South),
			),
			(
				(West, West, West, West),
				(West, West, West, West, North),
				(West, West, West, West, North, North),
				(West, West, West, West, North, North, North),
				(West, West, West, West, South, South, South, South),
				(West, West, West, West, South, South, South),
				(West, West, West, West, South, South),
				(West, West, West, West, South),
			),
			(
				(West, West, West),
				(West, West, West, North),
				(West, West, West, North, North),
				(West, West, West, North, North, North),
				(West, West, West, South, South, South, South),
				(West, West, West, South, South, South),
				(West, West, West, South, South),
				(West, West, West, South),
			),
			(
				(West, West),
				(West, West, North),
				(West, West, North, North),
				(West, West, North, North, North),
				(West, West, South, South, South, South),
				(West, West, South, South, South),
				(West, West, South, South),
				(West, West, South),
			),
			(
				(West,),
				(West, North),
				(West, North, North),
				(West, North, North, North),
				(West, South, South, South, South),
				(West, South, South, South),
				(West, South, South),
				(West, South),
			),
		)
	elif ws == 9:
		_moves = (
			(
				(),
				(North,),
				(North, North),
				(North, North, North),
				(North, North, North, North),
				(South, South, South, South),
				(South, South, South),
				(South, South),
				(South,),
			),
			(
				(East,),
				(East, North),
				(East, North, North),
				(East, North, North, North),
				(East, North, North, North, North),
				(East, South, South, South, South),
				(East, South, South, South),
				(East, South, South),
				(East, South),
			),
			(
				(East, East),
				(East, East, North),
				(East, East, North, North),
				(East, East, North, North, North),
				(East, East, North, North, North, North),
				(East, East, South, South, South, South),
				(East, East, South, South, South),
				(East, East, South, South),
				(East, East, South),
			),
			(
				(East, East, East),
				(East, East, East, North),
				(East, East, East, North, North),
				(East, East, East, North, North, North),
				(East, East, East, North, North, North, North),
				(East, East, East, South, South, South, South),
				(East, East, East, South, South, South),
				(East, East, East, South, South),
				(East, East, East, South),
			),
			(
				(East, East, East, East),
				(East, East, East, East, North),
				(East, East, East, East, North, North),
				(East, East, East, East, North, North, North),
				(East, East, East, East, North, North, North, North),
				(East, East, East, East, South, South, South, South),
				(East, East, East, East, South, South, South),
				(East, East, East, East, South, South),
				(East, East, East, East, South),
			),
			(
				(West, West, West, West),
				(West, West, West, West, North),
				(West, West, West, West, North, North),
				(West, West, West, West, North, North, North),
				(West, West, West, West, North, North, North, North),
				(West, West, West, West, South, South, South, South),
				(West, West, West, West, South, South, South),
				(West, West, West, West, South, South),
				(West, West, West, West, South),
			),
			(
				(West, West, West),
				(West, West, West, North),
				(West, West, West, North, North),
				(West, West, West, North, North, North),
				(West, West, West, North, North, North, North),
				(West, West, West, South, South, South, South),
				(West, West, West, South, South, South),
				(West, West, West, South, South),
				(West, West, West, South),
			),
			(
				(West, West),
				(West, West, North),
				(West, West, North, North),
				(West, West, North, North, North),
				(West, West, North, North, North, North),
				(West, West, South, South, South, South),
				(West, West, South, South, South),
				(West, West, South, South),
				(West, West, South),
			),
			(
				(West,),
				(West, North),
				(West, North, North),
				(West, North, North, North),
				(West, North, North, North, North),
				(West, South, South, South, South),
				(West, South, South, South),
				(West, South, South),
				(West, South),
			),
		)

def move_to(goal_x, goal_y, start_x=get_pos_x(), start_y=get_pos_y()):
	dx = goal_x - start_x
	dy = goal_y - start_y
	for fx in _moves[dx][dy]:
		move(fx)

def move_to_pos(goal_pos, start_pos):
	goal_x, goal_y = goal_pos
	start_x, start_y = start_pos
	move_to(goal_x, goal_y, start_x, start_y)


world_size = get_world_size()

def init_grid(SIZE=get_world_size()):
	grid = {}
	for x in range(SIZE):
		grid[x] = {}
		for y in range(SIZE):
			till()
			plant(Entities.Cactus)
			grid[x][y] = measure()
			move(North)
		move(East)
	return grid

def sort_and_farm_cacti():
	grid = init_grid()
	insertion_sort(grid)
	move_to(0,0)
	harvest()

def farm_cacti(target_value = 1000000):
	set_world_size(8)
	update()
	move_to(0, 0)
	while num_items(Items.Cactus) < target_value:
		sort_and_farm_cacti()

def plant_one():
	if can_harvest():
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Cactus)

def prune():
	if get_entity_type() != Entities.Cactus:
		plant_one()
	while measure() < 4:
		plant_one()
		use_item(Items.Fertilizer)

def prune_all():
	move_to(0, 0)
	size = get_world_size()
	for i in range(size):
		for j in range(size):
			prune()
			move(North)
		move(East)

def plant_all():
	move_to(0, 0)
	size = get_world_size()
	for i in range(size):
		for j in range(size):
			plant_one()
			move(North)
		move(East)

def harvest_one():
	if can_harvest():
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()

def harvest_all():
	move_to(0, 0)
	size = get_world_size()
	for i in range(size):
		for j in range(size):
			harvest_one()
			move(North)
		move(East)

def sort_all():
	size = get_world_size()
	x, y = get_pos_x(), get_pos_y()
	move_to(0, 0)
	# bottom to top
	for x_pos in range(size):
	# perform each swap size - 1 times
		for y_pos in range(size):
			current_measure = measure()
			if y_pos > 0 and current_measure < measure(South):
				swap(South)
			if y_pos < size - 1 and current_measure > measure(North):
				swap(North)
			if x_pos > 0 and current_measure < measure(West):
				swap(West)
			if x_pos < size - 1 and current_measure > measure(East):
				swap(East)
			move(North)
		move(North)
	move(East)
	# left to right
	for y_pos in range(size):
		# perform each swap size - 1 times
		for x_pos in range(size):
			current_measure = measure()
			if y_pos > 0 and current_measure < measure(South):
				swap(South)
			if y_pos < size - 1 and current_measure > measure(North):
				swap(North)
			if x_pos > 0 and current_measure < measure(West):
				swap(West)
			if x_pos < size - 1 and current_measure > measure(East):
				swap(East)
			move(East)
		move(East)
	move(North)


def insertion_sort(grid):
	ws = get_world_size()
	rn = range(ws)
	n1 = ws - 1
	rrn = range(n1, -1, -1)

	def insert_low(x, y):
		cur = grid[x][y]
		if x:
			if y:
				left = grid[x - 1][y]
				down = grid[x][y - 1]
				if cur < left or cur < down:
					move_to(x, y)
					while cur < left or cur < down:
						if left > down:
							swap(West)
							grid[x][y] = left
							x -= 1
							grid[x][y] = cur
							if x:
								move(West)
								left = grid[x - 1][y]
								down = grid[x][y - 1]
							else:
								break
						else:
							swap(South)
							grid[x][y] = down
							y -= 1
							grid[x][y] = cur
							if y:
								move(South)
								left = grid[x - 1][y]
								down = grid[x][y - 1]
							else:
								break
		if x:
			if cur < grid[x - 1][y]:
				move_to(x, y)
				while cur < grid[x - 1][y]:
					swap(West)
					grid[x][y] = grid[x - 1][y]
					x -= 1
					grid[x][y] = cur
					if x:
						move(West)
					else:
						break
		if y:
			if cur < grid[x][y - 1]:
				li = grid[x]
				move_to(x, y)
				while cur < li[y - 1]:
					swap(South)
					li[y] = li[y - 1]
					y -= 1
					li[y] = cur
					if y:
						move(South)
					else:
						break

	def insert_high(x, y):
		cur = grid[x][y]
		if x < n1:
			if y < n1:
				right = grid[x + 1][y]
				up = grid[x][y + 1]
				if cur > right or cur > up:
					move_to(x, y)
					while cur > right or cur > up:
						if right < up:
							swap(East)
							grid[x][y] = right
							x += 1
							grid[x][y] = cur
							if x < n1:
								move(East)
								right = grid[x + 1][y]
								up = grid[x][y + 1]
							else:
								break
						else:
							swap(North)
							grid[x][y] = up
							y += 1
							grid[x][y] = cur
							if y < n1:
								move(North)
								right = grid[x + 1][y]
								up = grid[x][y + 1]
							else:
								break
		if x < n1:
			if cur > grid[x + 1][y]:
				move_to(x, y)
				while cur > grid[x + 1][y]:
					swap(East)
					grid[x][y] = grid[x + 1][y]
					x += 1
					grid[x][y] = cur
					if x + 1 < ws:
						move(East)
					else:
						break
		if y < n1:
			if cur > grid[x][y + 1]:
				li = grid[x]
				move_to(x, y)
				while cur > li[y + 1]:
					swap(North)
					li[y] = li[y + 1]
					y += 1
					li[y] = cur
					if y < n1:
						move(North)
					else:
						break
	for size in range(5):
		for x in rn:
			gridx = grid[x]
			for y in rn:
				if gridx[y] == size:
					insert_low(x, y)
		size = 9 - size
		for x in rrn:
			gridx = grid[x]
			for y in rrn:
				if gridx[y] == size:
					insert_high(x, y)
