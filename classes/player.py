import math

from classes.particles import Punch, Bullet
from constants import *
from sprite_groups import entities, interactive, moving
from functions import get_dist, load_image


class Player(pygame.sprite.Sprite):
    def __init__(self, player_image: pygame.Surface, pos_x: int, pos_y: int, speed: int = 5):
        super().__init__()
        self.image = player_image
        self.x, self.y = pos_x, pos_y
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.speed = speed
        self.hp = 100
        self.max_hp = 100
        self.damage_melee = 10
        self.damage_ranged = 5
        self.money = 0
        self.attack_cooldown = FPS
        self.moved = False

    def key_pressed(self, all_keys, current_tick_keys, current_tick_mouse):
        for key in all_keys:
            if key in MOVE_KEYS:
                self.move(key)
            elif key in current_tick_keys:
                if key == ACTIVE_KEYS["interaction"]:
                    self.interact()
                elif key == ACTIVE_KEYS["attack_melee"]:
                    self.attack_melee()
        if 1 in current_tick_mouse:
            self.attack_ranged()

    def move(self, key):
        if not self.moved: self.moved = True
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

        if pygame.sprite.spritecollideany(self, entities) or len(
                pygame.sprite.spritecollide(self, moving, False)) > 1 or any(
            cord < 0 or cord + delta > MAP_SIZE_PIXELS for cord, delta in
            ((self.x, self.rect.width), (self.y, self.rect.height))):
            self.rect.x -= delta_x
            self.rect.y -= delta_y

            self.x -= delta_x
            self.y -= delta_y

    def interact(self) -> None:
        to_interact = list(filter(lambda x: get_dist(self.rect, x.rect) <= INTERACT_DISTANCE, interactive))

        if to_interact:
            min(to_interact, key=lambda x: get_dist(self.rect, x.rect)).interaction()

    def attack_melee(self) -> None:
        mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()
        distance = get_dist(mouse_pos, self.rect.center)
        x = self.rect.centerx + (mouse_x - self.rect.centerx) / distance * CELL_SIZE
        y = self.rect.centery + (mouse_y - self.rect.centery) / distance * CELL_SIZE
        Punch(self, x, y, animation_speed=1)

    def attack_ranged(self) -> None:
        mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()
        distance = get_dist(mouse_pos, self.rect.center)
        delta_x = -self.rect.centerx + mouse_x
        delta_y = self.rect.centery - mouse_y

        angle = math.acos(delta_x / distance)

        if delta_y < 0:
            angle = 2 * math.pi - angle

        Bullet(self, load_image("other/bullet.png", do_resize=False), self.rect.centerx, self.rect.centery, angle)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)

    def get_damage(self, dmg: int):
        self.hp -= dmg
        if self.hp <= 0:
            print("dead", self.hp)

    def deal_damage(self, target):
        target.get_damage(self.damage_ranged)

    def get_hp_percents(self) -> float:
        return self.hp / self.max_hp

    def get_money(self) -> int:
        return self.money

    def use_money(self, cost: int) -> None:
        self.money -= cost

    def add_money(self, money: int) -> None:
        self.money += money

    def is_alive(self) -> bool:
        return player.hp > 0

player = Player(load_image("entities/mar.png", (45, 45)), WIDTH / 2, HEIGHT / 2)
moving.add(player)
