import os

from classes.cell import Cell
from constants import FPS


class Punch(Cell):
    def __init__(self, pos_x: int, pos_y: int, animation_speed: int = FPS):
        image = iter(map(lambda x: "other/punches/" + x, os.listdir("data/other/punches")))
        super().__init__(image, pos_x, pos_y, animation_speed=animation_speed)

