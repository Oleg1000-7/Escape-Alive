import pygame.sprite

from classes.map_objects import init_map
from classes.text import Text
from constants import *
from functions import *
from classes.camera import Camera
from sprite_groups import *
from classes.player import player, Player, create_player

pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

def menu():
    fon = load_image('other/bg.jpg', (WIDTH, 0))
    screen.fill(fon.get_at((0, 0)))
    screen.blit(fon, (0, HEIGHT - fon.get_height()))
    font = pygame.font.Font(None, 30)

    string_rendered = font.render("Нажмите Enter, чтобы начать", 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(string_rendered, intro_rect)
    menu_flag = True
    while menu_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu_flag = False
                    break
        pygame.display.flip()
        clock.tick(FPS)
    game()

def game():
    wm = generate_map()

    init_map(wm, enemies_count=45)
    camera = Camera()

    def draw_hud(screen, buffs: list[pygame.Surface, (int, int)] | list):
        for surf, coord in buffs:
            screen.blit(surf, surf.get_rect().move(*coord))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20, 20, 70 + WIDTH / 10, HEIGHT / 15))
        pygame.draw.rect(screen, RED, pygame.Rect(20, 20, (70 + (WIDTH / 10)) * player.get_hp_percents(), HEIGHT / 15))
        gold.set_text(str(player.get_money()))

    create_player(player)
    moving.add(player)
    gold = Text(str(player.get_money()), WIDTH // 2, 20, BLACK, sprite_like=False)

    while True:
        events = pygame.event.get()
        key_events = list(map(lambda e: e.type, events))
        mouse_key_pressed_current_tick = list(
            map(lambda e: e.button, filter(lambda e: e.type == pygame.MOUSEBUTTONDOWN, events)))
        keys_pressed_current_tick = list(map(lambda e: e.key, filter(lambda e: e.type == pygame.KEYDOWN, events)))

        if pygame.QUIT in key_events or pygame.K_ESCAPE in keys_pressed_current_tick or player.get_hp() <= 0:
            menu()

        keys = filter(lambda x: pygame.key.get_pressed()[x], ACTIVE_KEYS.values())
        player.key_pressed(keys, keys_pressed_current_tick, mouse_key_pressed_current_tick)

        camera.update(player)
        for s in all_sprites:
            camera.apply(s)
        camera.apply(player)
        screen.fill(BLUE)
        all_sprites.draw(screen)
        player.draw(screen)
        all_sprites.update(screen)
        player.update()
        hud_elements.update(screen)

        draw_hud(screen, [])
        pygame.display.flip()
        clock.tick(FPS)

menu()
