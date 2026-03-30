from movement import *

GRASS = Grounds.Grassland
SOIL = Grounds.Soil

def prepare_farm(size): 
	for _ in range(size):
		for _ in range(size):
			if can_harvest():
				harvest()
				till()
			move(North)
		move(East)

def is_tree_tile():
	x, y = get_pos_x(), get_pos_y()
	return (x % 2 == 0 and y % 2 == 0) or ((x + y) % 2 == 0)

def harvest_energy():
	most_petals = 0
	harvest_y = None
	move_to(0, 0)
	for y in range(get_world_size()):
		if measure() > most_petals:
			harvest_y = y
			most_petals = measure()
	move_to(0, harvest_y)
	harvest()
	till()
	plant(Entities.Sunflower)

def handle_grass_tile():
	if can_harvest():
		harvest()
	if get_ground_type() != GRASS:
		clear()
		
def handle_tree_tile():
	if can_harvest():
		harvest()
	if get_ground_type() != GRASS:
		clear()
	if is_tree_tile():
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)

def handle_carrot_tile():
	if can_harvest():
		harvest()
	if get_ground_type() != SOIL:
		till()
	plant(Entities.Carrot)

def handle_pumpkin_tile():
	if can_harvest():
		harvest()
	if get_ground_type() != SOIL:
		till()
	if get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() != Entities.Pumpkin:
		plant(Entities.Pumpkin)
		return
	plant(Entities.Pumpkin)


def handle_cactus_tile():
	if can_harvest():
		harvest()
	if get_ground_type() != SOIL:
		till()
	plant(Entities.Cactus)


def run_function_by_item_type(t):
	if t == Items.Hay:
		handle_grass_tile()
	elif t == Items.Wood:
		handle_tree_tile()
	elif t == Items.Carrot:
		handle_carrot_tile()
	elif t == Items.Pumpkin:
		handle_pumpkin_tile()


def is_item(item_type):
	for item in Items:
		if(item_type == item):
			return True
	return False

def acquire_value_of_item(item_type, desired_value):
	if is_item(item_type):
		current_value = num_items(item_type)
		while current_value < desired_value:
			for i in range(get_world_size()):
				for j in range(get_world_size()):
					run_function_by_item_type(item_type)
					move(North)
				move(East)
			
			current_value = num_items(item_type)