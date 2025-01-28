from classes.cell import Cell
from sprite_groups import *


class Box(Cell):
    def __init__(self, pos_x: int, pos_y: int, size: tuple | int):
        super().__init__("box.png", pos_x, pos_y, size, hit_box=True, groups=entities)

class Grass(Cell):
    def __init__(self, pos_x: int, pos_y: int, size: tuple | int):
        super().__init__("grass.png", pos_x, pos_y, size, hit_box=False)

CLASSES_SIMPLES = [Grass, Box]
