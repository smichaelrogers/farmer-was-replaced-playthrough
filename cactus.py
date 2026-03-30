from movement import *

def farm_cacti(target_value = 100000):
	while num_items(Items.Cactus < target_value):
		plant_all()
		prune_all()
		sort_all()
		harvest_all()

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
	for _ in range(4):
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