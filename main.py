from movement import *
from cactus import farm_cacti
from maze import farm_gold
from hay import farm_hay
from wood import farm_wood
from carrot import farm_carrot
from pumpkin import farm_pumpkin
from cactus import farm_cacti
from weird_susbstance import farm_weird_substance
from dinosaur import farm_bone
from sunflower import farm_power

target_values = {
	Items.Hay: 20000000,
	Items.Wood: 100000000,
	Items.Carrot: 10000000,
	Items.Pumpkin: 100000,
	Items.Cactus: get_cost(Unlocks.Mazes)[Items.Cactus],
	Items.Bone: get_cost(Unlocks.Polyculture)[Items.Bone],
	Items.Gold: get_cost(Unlocks.Megafarm)[Items.Gold],
	Items.Weird_Substance: 200000,
	Items.Power: 10000,
}

handlers = {
	Items.Hay: farm_hay,
	Items.Wood: farm_wood,
	Items.Carrot: farm_carrot,
	Items.Pumpkin: farm_pumpkin,
	Items.Cactus: farm_cacti,
	Items.Bone: farm_bone,
	Items.Gold: farm_gold,
	Items.Weird_Substance: farm_weird_substance,
	Items.Power: farm_power
}

def start():
	clear()
	move_to(0, 0)
	set_world_size(8)
	do_a_flip()

	for key in handlers:
		handlers[key](target_values[key])

start()