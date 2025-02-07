import json
import pygame


BLACK = pygame.Color("#000000")
WHITE = pygame.Color("#ffffff")
RED = pygame.Color("#ff0000")
GREEN = pygame.Color("#00ff00")
BLUE = pygame.Color("#0000ff")
SIZE = WIDTH, HEIGHT = (500, 500)
CELL_SIZE = 50
INTERACT_DISTANCE = CELL_SIZE * 1.5
MAP_SIZE_CELLS = 64
MAP_SIZE_PIXELS = CELL_SIZE * MAP_SIZE_CELLS
FPS = 60
ENEMIES_ATTACK_COOLDOWN = 1 * 1000
ENEMIES_AGRO_DISTANCE = CELL_SIZE * 10

with open("key_binds.json", "r", encoding="utf-8") as keys_file:
    keys = json.load(keys_file)
ACTIVE_KEYS = {key: eval(f"pygame.{value}") for key, value in keys.items()}
MOVE_KEYS = [ACTIVE_KEYS["up"], ACTIVE_KEYS["left"], ACTIVE_KEYS["down"], ACTIVE_KEYS["right"]]
