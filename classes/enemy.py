from classes.entity import Entity
from constants import CELL_SIZE
from functions import get_sprite_dist
from sprite_groups import entities


class Enemy(Entity):
    def __init__(self, image, pos_x, pos_y, hp, speed=0, agro_distance=CELL_SIZE * 10):
        super().__init__(image, pos_x, pos_y, hp, groups=entities)
        self.speed = speed
        self.agro_dist = agro_distance

    def update(self):
        if self.agro_dist < get_sprite_dist(self.rect, player.rect): self.move()

    def move(self):
        rect_p = player.rect


    def attack(self):
        pass