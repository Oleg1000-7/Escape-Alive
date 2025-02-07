import pygame.time
from pygame.sprite import spritecollide

from classes.entity import Entity
from constants import ENEMIES_ATTACK_COOLDOWN, ENEMIES_AGRO_DISTANCE
from functions import get_sprite_dist
from sprite_groups import entities, moving
from classes.player import player


class Enemy(Entity):
    def __init__(self, image, pos_x, pos_y, hp, speed=0, damage=5):
        super().__init__(image, pos_x, pos_y, hp, groups=moving)
        self.speed = speed
        self.agro_distance = ENEMIES_AGRO_DISTANCE
        self.stop_distance = max(self.rect.h, self.rect.w) // 4

        self.damage = damage
        self.previous_attack = 0
        self.do_attack = False

    def update(self):
        if player.moved:
            d = get_sprite_dist(self.rect, player.rect)
            if self.agro_distance > d: self.do_attack = self.move(d)
            if self.do_attack:
                self.attack()
                self.do_attack = False

    def move(self, d):
        collide_flag = False
        xp, yp = player.rect.center
        dx, dy = abs(self.rect.centerx - xp), abs(self.rect.centery - yp)

        sin = dx / d
        cos = dy / d

        if dx > self.stop_distance:
            delta_x = int(self.speed * sin if xp > self.rect.centerx else -self.speed * sin)
            self.rect.x += delta_x

            if spritecollide(self, entities, False) or len(spritecollide(self, moving, False)) > 1:
                self.rect.x -= delta_x
                collide_flag = True

        if dy > self.stop_distance:
            delta_y = int(self.speed * cos if yp > self.rect.centery else -self.speed * cos)
            self.rect.y += delta_y

            if spritecollide(self, entities, False) or len(spritecollide(self, moving, False)) > 1:
                self.rect.y -= delta_y
                collide_flag = True

        return collide_flag

    def attack(self):
        current_tick = pygame.time.get_ticks()
        if current_tick - self.previous_attack > ENEMIES_ATTACK_COOLDOWN:
            player.deal_damage(self.damage)
            self.previous_attack = current_tick

