from classes.map_objects import CLASSES_SIMPLES
from constants import *
from functions import *
from classes.player import Player
from classes.camera import Camera
from sprite_groups import *


def init_map(world_map) -> None:
    print(world_map)
    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE):
            CLASSES_SIMPLES[world_map[i][j]](CELL_SIZE * j, CELL_SIZE * i, CELL_SIZE)


pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

init_map(generate_map())
player = Player(load_image("mar.png"), WIDTH / 2, HEIGHT / 2)
camera = Camera()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: terminate()

    for i in MOVE_KEYS:
        if pygame.key.get_pressed()[i]: player.move(i, entities)

    camera.update(player)
    for s in all_sprites:
        camera.apply(s)

    screen.fill(BLACK)
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)
