from movement import *
from cactus import farm_cacti
from maze import farm_treasure
from hay import farm_hay
from wood import farm_wood
from carrot import farm_carrot
from pumpkin import farm_pumpkin
from cactus import farm_cacti
from weird_susbstance import farm_weird_substance
from dinosaur import farm_bone

target_values = {
	Items.Hay: 20000000,
	Items.Wood: 80000000,
	Items.Carrot: 10000000,
	Items.Pumpkin: 100000,
	Items.Cactus: 200000,
	Items.Bone: 200000,
	Items.Weird_Substance: 200000,
	Items.Gold: 10000
}

def start():
	move_to(0, 0)
	do_a_flip()

	# farm_hay(target_values[Items.Hay])
	farm_wood(target_values[Items.Wood])
	farm_carrot(target_values[Items.Carrot])
	farm_pumpkin(target_values[Items.Pumpkin])
	farm_bone(target_values[Items.Bone])
	farm_weird_substance(target_values[Items.Weird_Substance])
	farm_cacti(target_values[Items.Cactus])
	farm_treasure(target_values[Items.Gold])

start()