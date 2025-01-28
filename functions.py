import sys
import os
import pygame

from constants import MAP_SIZE


def load_image(name: str) -> pygame.Surface:
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def terminate():
    pygame.quit()
    sys.exit()


import random


def generate_map() -> list[list[int]]:
    size = MAP_SIZE
    min_ones = 1
    max_ones = 4

    matrix = [[0 for _ in range(size)] for _ in range(size)]

    for row in range(size):
        num_ones = random.randint(min_ones, max_ones)
        ones_positions = random.sample(range(size), num_ones)

        for col in ones_positions:
            matrix[row][col] = 1

    for col in range(size):
        column = [matrix[row][col] for row in range(size)]
        if column.count(1) > max_ones:
            return generate_map()

    return matrix



