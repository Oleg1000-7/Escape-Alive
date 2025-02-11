import os
import random
from random import sample, randint
from typing import Type

import pygame

from classes.cell import Cell
from classes.enemy import Enemy
from classes.entity import Entity
from classes.interactive import Interactive
from classes.player import player
from classes.text import Text
from constants import MAP_SIZE_CELLS, CELL_SIZE
from functions import load_image
from sprite_groups import *


class Obstacle(Entity):
    def __init__(self, pos_x: int, pos_y: int, **kwargs):
        image = load_image(f"obstacles/{random.choice(("tree2.png", "tree2.png", "tree.png", "rock.png"))}",
                           do_resize=False)
        super().__init__(image, pos_x, pos_y + image.get_height() // 2, groups=entities, hp=500)


cost = 50


class LootBox(Interactive):
    def __init__(self, pos_x: int, pos_y: int, **kwargs):
        self.full_image = load_image("other/chest.png", (50, 25))
        w, h = self.size = self.full_image.get_size()
        image = self.full_image.subsurface(pygame.Rect((0, 0), (w / 2, h)))
        super().__init__(image, pos_x, pos_y)
        x, y = self.rect.bottomleft
        Text(str(cost), x, y, (255, 255, 0))

    def interaction(self):
        if player.money >= cost:
            w, h = self.size
            image = self.full_image.subsurface(pygame.Rect((w / 2, 0), (w / 2, h)))
            self.image = image


floor_image = load_image("floor/foliage3.png", (50, 50))
CLASSES_SIMPLES: dict[int, Type[Cell | Obstacle | LootBox]] = {
    0: None,
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
            Cell(floor_image, CELL_SIZE * x, CELL_SIZE * y)

    for y in range(MAP_SIZE_CELLS):
        for x in range(MAP_SIZE_CELLS):
            o_type = CLASSES_SIMPLES[w_map[y][x]]
            if o_type:
                o_type(pos_x=CELL_SIZE * x, pos_y=CELL_SIZE * y)

    while enemies_count > 0:
        for y in range(MAP_SIZE_CELLS):
            for x in range(MAP_SIZE_CELLS):
                if not w_map[y][x] and randint(1, 100) == 1:
                    Enemy(list(
                        map(lambda name: "entities/enemy_slime/" + name, os.listdir("data/entities/enemy_slime"))),
                          CELL_SIZE * x, CELL_SIZE * y, 10, 1)
                    enemies_count -= 1
                if enemies_count <= 0: break
