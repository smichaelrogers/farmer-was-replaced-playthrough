from movement import *

world_size = get_world_size()

def sort_and_farm_cacti():
	clear()
	move_to(0, 0)
	shear_sort(simple_planting())
	harvest()

def simple_planting(SIZE=get_world_size()):
	grid = {}
	for x in range(SIZE):
		grid[x] = {}
		for y in range(SIZE):
			till()
			plant(Entities.Cactus)
			grid[x][y] = measure()
			move(North)
		move(East)
	prune_all()
	return grid

def shear_sort(grid):
	# Row phase: snake-order sort on each row.
	for i in range(world_size):
		if i % 2 == 0:
			changed = True
			while changed:
				changed = False
				# Even row: ascending (South → North, i.e. increasing j)
				for j in range(world_size):
					if j<world_size - 1:
						if grid[i][j] > grid[i][j+1]:
							move_to(i, j)
							swap(North)  # swap with neighbor at (i, j+1)
							grid[i][j], grid[i][j+1] = grid[i][j+1], grid[i][j]
							changed = True
					if i<world_size - 1:
						if grid[i][j] > grid[i+1][j]:
							move_to(i, j)
							swap(East)  # swap with neighbor at (i+1, j)
							grid[i][j], grid[i+1][j] = grid[i+1][j], grid[i][j]
							changed = True
		else:
			changed = True
			while changed:
				changed = False
				# Odd row: descending (North → South, i.e. decreasing j)
				for j in range(world_size-1, 0, -1):
					if j>0:
						if grid[i][j] < grid[i][j-1]:
							move_to(i, j)
							swap(South)  # swap with neighbor at (i, j-1)
							grid[i][j], grid[i][j-1] = grid[i][j-1], grid[i][j]
							changed = True
					if i<world_size - 1:
						if grid[i][j] > grid[i+1][j]:
							move_to(i, j)
							swap(East)  # swap with neighbor at (i+1, j)
							grid[i][j], grid[i+1][j] = grid[i+1][j], grid[i][j]
							changed = True

	# Column phase: sort each column in ascending order (West → East, i.e. increasing i)
	for j in range(world_size):
		changed = True
		while changed:
			changed = False
			for i in range(world_size - 1):
				if grid[i][j] > grid[i+1][j]:
					move_to(i, j)
					swap(East)  # swap with neighbor at (i+1, j)
					grid[i][j], grid[i+1][j] = grid[i+1][j], grid[i][j]
					changed = True
	return grid

def farm_cacti(target_value = 100000):
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