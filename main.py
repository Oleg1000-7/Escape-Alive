import pygame

from classes.interactive import Interactive
from classes.map_objects import CLASSES_SIMPLES
from constants import *
from functions import *
from classes.player import Player
from classes.camera import Camera
from sprite_groups import *


def init_map(world_map) -> None:
    w_map, o_map = world_map
    for o in random.sample(o_map, 10): #lootbox
        w_map[o[0]][o[1]] = 11
        o_map.remove(o)

    #w_map[int(WIDTH / 2 / CELL_SIZE)][int(HEIGHT / 2 / CELL_SIZE)] = 1

    for y in range(MAP_SIZE_CELLS):
        for x in range(MAP_SIZE_CELLS):
            o_type = CLASSES_SIMPLES[w_map[y][x]]
            if issubclass(o_type, Interactive):
                CLASSES_SIMPLES[current_ground_class](CELL_SIZE * x, CELL_SIZE * y)
            o_type(CELL_SIZE * x, CELL_SIZE * y)


pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

current_ground_class = 0
wm = generate_map()
WM = wm

while not wm:
    wm = generate_map()

init_map(wm)

player = Player(load_image("mar.png"), WIDTH / 2, HEIGHT / 2)
camera = Camera()
while True:
    events = pygame.event.get()
    key_events = list(map(lambda e: e.type, events))
    keys_pressed_current_tick = list(map(lambda e: e.key, filter(lambda e: e.type == pygame.KEYDOWN, events)))

    if pygame.QUIT in key_events or pygame.K_ESCAPE in keys_pressed_current_tick: terminate()

    for i in ACTIVE_KEYS.values():
        if pygame.key.get_pressed()[i]: player.key_pressed(i, keys_pressed_current_tick)

    camera.update(player)
    for s in all_sprites:
        camera.apply(s)

    screen.fill(BLACK)
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)
