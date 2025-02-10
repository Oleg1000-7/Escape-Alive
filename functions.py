import sys
import os
import pygame
import random

from constants import MAP_SIZE_CELLS, WIDTH, HEIGHT


def resize_image(img, size=(50, 50)):
    return pygame.transform.scale(img, size)


def load_image(name: str, size_expected: int | tuple[int, int] | None = None, do_resize: bool = True) -> pygame.Surface:
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        fullname = "data/default.jpg"

    image = pygame.image.load(fullname)

    if do_resize:
        if size_expected and image.get_size() != (
                size_expected if isinstance(size_expected, tuple) else (size_expected, size_expected)):
            image = resize_image(image, size_expected)
        else:
            image = resize_image(image)
    return image


def terminate():
    pygame.quit()
    sys.exit()


def generate_map(fill: int = 0) -> tuple[list[list[int]], list[tuple]] | None:
    size = MAP_SIZE_CELLS
    min_ones = 1
    max_ones = 4
    while True:
        matrix = [[fill for _ in range(size)] for _ in range(size)]
        objects = list()

        for row in range(size):
            num_ones = random.randint(min_ones, max_ones)
            ones_positions = random.sample(range(size), num_ones)

            for col in ones_positions:
                matrix[row][col] = 1
                objects.append((row, col))

        for col in range(size):
            column = [matrix[row][col] for row in range(size)]
            if column.count(1) > max_ones:
                continue

        if matrix[int(WIDTH / 2 / size)][int(HEIGHT / 2 / size)] == 1:
            continue

        return matrix, objects


def get_dist(rect1: pygame.rect.Rect | tuple[int, int], rect2: pygame.rect.Rect | tuple[int, int]):
    if isinstance(rect1, tuple):
        return ((rect1[0] - rect2[0]) ** 2 + (rect1[1] - rect2[1]) ** 2) ** 0.5
    return ((rect1.x - rect2.x) ** 2 + (rect1.y - rect2.y) ** 2) ** 0.5
