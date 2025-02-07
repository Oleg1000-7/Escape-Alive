from typing import Type

from classes.cell import Cell
from classes.interactive import Interactive
from sprite_groups import *


class Obstacle(Cell):
    def __init__(self, pos_x: int, pos_y: int, **kwargs):
        super().__init__("box.png", pos_x, pos_y, hit_box=True, groups=entities)

class LootBox(Interactive):
    def __init__(self, pos_x: int, pos_y: int, **kwargs):
        super().__init__("default.jpg", pos_x, pos_y)


CLASSES_SIMPLES: dict[int, Type[Cell | Obstacle | LootBox]] = {
    0: Cell,
    1: Obstacle,
    11: LootBox
}
