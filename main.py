from movement import *
from cactus import farm_cacti
from maze import farm_gold
from hay import farm_hay
from wood import farm_wood
from carrot import farm_carrot
from pumpkin import farm_pumpkin
from cactus import farm_cacti
from weird_substance import farm_weird_substance
from dinosaur import farm_bone
from sunflower import farm_power

ONE_MILLION = 1000000

target_values = {
	Items.Power: 16000,
	Items.Hay: ONE_MILLION * 10,
	Items.Wood: ONE_MILLION * 100,
	Items.Carrot: ONE_MILLION * 100,
	Items.Pumpkin: ONE_MILLION * 30,
	Items.Cactus: ONE_MILLION * 16,
	Items.Bone: ONE_MILLION * 2,
	Items.Gold: 128000,
	Items.Weird_Substance: ONE_MILLION,
}

handlers = {
	Items.Power: farm_power,
	Items.Hay: farm_hay,
	Items.Wood: farm_wood,
	Items.Carrot: farm_carrot,
	Items.Pumpkin: farm_pumpkin,
	Items.Cactus: farm_cacti,
	Items.Bone: farm_bone,
	Items.Gold: farm_gold,
	Items.Weird_Substance: farm_weird_substance,
}

def start():
	clear()
	move_to(0, 0)
	set_world_size(8)
	do_a_flip()

	for key in handlers:
		handlers[key](target_values[key])

start()