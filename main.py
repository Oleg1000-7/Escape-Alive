from constants import *
from functions import *
from classes.player import Player


all_sprites = pygame.sprite.Group()
entities = pygame.sprite.Group()
moving = pygame.sprite.Group()

pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
player = Player(all_sprites, load_image("mar.png"), WIDTH / 2, HEIGHT / 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: terminate()
    for i in MOVE_KEYS:
        if pygame.key.get_pressed()[i]: player.move(i, entities)

    screen.fill(BLACK)
    all_sprites.draw(screen)
    all_sprites.update(clock.tick())
    pygame.display.flip()
    clock.tick(FPS)
