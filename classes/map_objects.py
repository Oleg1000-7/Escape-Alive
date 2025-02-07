from random import sample, randint
from typing import Type

from classes.cell import Cell
from classes.enemy import Enemy
from classes.interactive import Interactive
from constants import MAP_SIZE_CELLS, CELL_SIZE
from functions import load_image
from sprite_groups import *


class Obstacle(Cell):
    def __init__(self, pos_x: int, pos_y: int, **kwargs):
        super().__init__(load_image("box.png", (50, 50)), pos_x, pos_y, hit_box=True, groups=entities)

class LootBox(Interactive):
    def __init__(self, pos_x: int, pos_y: int, **kwargs):
        super().__init__(load_image("default.jpg", (50, 50)), pos_x, pos_y)


floor_image = load_image("grass.png", (50, 50))
CLASSES_SIMPLES: dict[int, Type[Cell | Obstacle | LootBox]] = {
    0: Cell,
    1: Obstacle,
    11: LootBox
}

def init_map(world_map, enemies_count=0) -> None:
    w_map, o_map = world_map
    for o in sample(o_map, 10):  # lootbox
        w_map[o[0]][o[1]] = 11
        o_map.remove(o)

    # w_map[int(WIDTH / 2 / CELL_SIZE)][int(HEIGHT / 2 / CELL_SIZE)] = 1

    for y in range(MAP_SIZE_CELLS):
        for x in range(MAP_SIZE_CELLS):
            o_type = CLASSES_SIMPLES[w_map[y][x]]
            if not o_type:
                Cell(floor_image, CELL_SIZE * x, CELL_SIZE * y)
            o_type(pos_x=CELL_SIZE * x, pos_y=CELL_SIZE * y, image=floor_image, hit_box=False)

    while enemies_count > 0:
        for y in range(MAP_SIZE_CELLS):
            for x in range(MAP_SIZE_CELLS):
                if not w_map[y][x] and randint(1, 10) == 1:
                    Enemy(load_image("-", (50, 50)), CELL_SIZE * x, CELL_SIZE * y, 100, 3)
                    enemies_count -= 1
                if enemies_count <= 0: break

