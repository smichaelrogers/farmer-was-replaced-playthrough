from movement import *

def dynamic_planting_with_companions(grid):
	while True:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if get_entity_type() == Entities.Grass:
					companion = get_companion()
					if companion != None:
						plant_type, (x, y) = companion
						print("Companion:", plant_type, "at", x, ",", y)
						move_to(x, y)
						grid[x][y] = (i, j)
						run_corresponding_function(plant_type)