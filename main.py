import pygame.sprite

from classes.map_objects import init_map
from constants import *
from functions import *
from classes.camera import Camera
from sprite_groups import *
from classes.player import player, draw_hud

pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

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

    draw_hud(screen, [])
    pygame.display.flip()
    clock.tick(FPS)
