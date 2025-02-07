import pygame.sprite
from random import randint

from classes.cell import Cell
from classes.enemy import Enemy
from classes.interactive import Interactive
from classes.map_objects import CLASSES_SIMPLES
from constants import *
from functions import *
from classes.camera import Camera
from sprite_groups import *
from classes.player import player


def init_map(world_map, enemies_count=0) -> None:
    w_map, o_map = world_map
    for o in random.sample(o_map, 10):  # lootbox
        w_map[o[0]][o[1]] = 11
        o_map.remove(o)

    # w_map[int(WIDTH / 2 / CELL_SIZE)][int(HEIGHT / 2 / CELL_SIZE)] = 1

    for y in range(MAP_SIZE_CELLS):
        for x in range(MAP_SIZE_CELLS):
            o_type = CLASSES_SIMPLES[w_map[y][x]]
            if issubclass(o_type, Interactive):
                Cell(floor_image, CELL_SIZE * x, CELL_SIZE * y)
            o_type(pos_x=CELL_SIZE * x, pos_y=CELL_SIZE * y, image=floor_image, hit_box=False)

    while enemies_count > 0:
        for y in range(MAP_SIZE_CELLS):
            for x in range(MAP_SIZE_CELLS):
                if not w_map[y][x] and randint(1, 10) == 1:
                    Enemy("-", CELL_SIZE * x, CELL_SIZE * y, 100, 3)
                    enemies_count -= 1
                if enemies_count <= 0: break


pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

floor_image = "grass.png"
wm = generate_map()
WM = wm

while not wm:
    wm = generate_map()

init_map(wm, enemies_count=10)
camera = Camera()

while True:
    events = pygame.event.get()
    key_events = list(map(lambda e: e.type, events))
    keys_pressed_current_tick = list(map(lambda e: e.key, filter(lambda e: e.type == pygame.KEYDOWN, events)))

    if pygame.QUIT in key_events or pygame.K_ESCAPE in keys_pressed_current_tick: terminate()

    keys = filter(lambda x: pygame.key.get_pressed()[x], ACTIVE_KEYS.values())
    player.key_pressed(keys, keys_pressed_current_tick)

    camera.update(player)
    for s in all_sprites:
        camera.apply(s)
    camera.apply(player)
    screen.fill(BLUE)
    all_sprites.draw(screen)
    player.draw(screen)
    all_sprites.update()
    player.update()
    pygame.display.flip()
    clock.tick(FPS)
