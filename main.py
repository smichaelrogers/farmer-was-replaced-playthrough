from movement import *
from farming import *
import cactus

def farm_cactus():
	cactus.plant_all()
	cactus.prune_all()
	cactus.sort_all()
	cactus.harvest_all()

def start():
	do_a_flip()
	change_hat(Hats.Cactus_Hat)
	while True:
		
		acquire_value_of_item(Items.Hay, 5000000)
		acquire_value_of_item(Items.Wood, 8000000)
		acquire_value_of_item(Items.Carrot, 1000000)
		acquire_value_of_item(Items.Pumpkin, 64000)
		acquire_value_of_item(Items.Cactus, 10000)


def test1():
	size = get_world_size() - 1
	move_to(0, 0)
	do_a_flip()
	move_to(size, size)
	do_a_flip()
	move_to(0, size)
	do_a_flip()
	move_to(size, 0)
	do_a_flip()
	move_to_start()
	do_a_flip()

def test2():
	size = get_world_size()
	for i in range(size):
		for j in range(size):
			print(i, j)

# test1()
# test2()
start()