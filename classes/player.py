from classes.sprite_base import SpriteObject
from constants import *
from sprite_groups import entities, interactive
from functions import get_sprite_dist


class Player(SpriteObject):
    def __init__(self, player_image: pygame.Surface, pos_x: int, pos_y: int, speed: int=10):
        super().__init__()
        self.image = player_image
        self.x, self.y = pos_x, pos_y
        self.rect  = self.image.get_rect().move(pos_x, pos_y)
        self.speed = speed

    def key_pressed(self, key, current_tick_keys):
        if key in MOVE_KEYS:
            self.move(key)
        elif key in current_tick_keys:
            if key == ACTIVE_KEYS["interaction"]: self.interact()

    def move(self, key):
        delta_x, delta_y = 0, 0

        if key == ACTIVE_KEYS["up"]:
            delta_x, delta_y = 0, -self.speed
        if key == ACTIVE_KEYS["down"]:
            delta_x, delta_y = 0, self.speed
        if key == ACTIVE_KEYS["left"]:
            delta_x, delta_y = -self.speed, 0
        if key == ACTIVE_KEYS["right"]:
            delta_x, delta_y = self.speed, 0

        self.rect.x += delta_x
        self.rect.y += delta_y
        self.x += delta_x
        self.y += delta_y

        if pygame.sprite.spritecollideany(self, entities) or any(
                cord < 0 or cord + delta > MAP_SIZE_PIXELS for cord, delta in ((self.x, self.rect.width), (self.y, self.rect.height))):
            self.rect.x -= delta_x
            self.rect.y -= delta_y
            self.x -= delta_x
            self.y -= delta_y

    def interact(self):
        for obj in interactive:
            if get_sprite_dist(self.rect, obj.rect) <= INTERACT_DISTANCE:
                obj.interaction()