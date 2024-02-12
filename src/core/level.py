# -*- coding: utf-8 -*-
"""
    This is the file of Level class
"""
__version__ = '0.1.0'
__author__ = 'Katarzyna Matuszek'

from math import sin, cos, pi
from src.core.spaceship import Spaceship
from src.core.eye import Eye
from src.core.bullet import BulletTypes, Bullet

class Level(object):

    def __init__(self):
        # Reset
        self.clean()

    def clean(self):
        # Entities
        self.spaceship = Spaceship([0,0,0])
        self.boss = Eye([0,10,-30])
        self.bullets = []
        # Patterns
        self.count = 0              # some kind of cooldown
        self.pattern_count = 0      # how many waves in a pattern
        self.bullets_now = 1        # current type of bullets
    
    # WARNING - pretty trashy code
    def update(self, input_object, delta_time):
        self.spaceship.update(input_object, delta_time)

        # Update existing bullets
        for bullet in self.bullets:
            
            bullet.update()

            # check borders
            if bullet.position[0] < -64 or bullet.position[0] > 64:
                bullet.has_hit = True
            if bullet.position[1] < -41 or bullet.position[1] > 41:
                bullet.has_hit = True
            if bullet.position[2] < -30 or bullet.position[2] > 35:
                bullet.has_hit = True

            # check hits
            if bullet.type == BulletTypes.PLAYER:
                if bullet.is_colliding(self.boss, 5):
                    self.boss.health -= 5
                    bullet.has_hit = True
            else:
                if bullet.is_colliding(self.spaceship, 3):
                    self.spaceship.health -= 3
                    bullet.has_hit = True

        # Generate new enemy bullets
        if self.count == 75:
            self.generate_wave(BulletTypes(self.bullets_now))
            self.pattern_count += 1
            self.count = 0

        # Generate new player bullets
        if self.count % 37 == 0:
            self.generate_wave(BulletTypes.PLAYER)

        # Pattern change
        if self.pattern_count == 15:
            self.bullets_now += 1
            if self.bullets_now > 3:
                self.bullets_now = 1
            self.pattern_count = 0

        self.count += 1

    def generate_wave(self, bullet_type):
        if (bullet_type == BulletTypes.PLAYER):
            bullet_pos = list(self.spaceship.position)
            bullet_pos[2] -= 4
            self.bullets.append(Bullet(bullet_pos, BulletTypes.PLAYER))
        else:
            pos = list(self.boss.position)
            pos[2] += 6
            radius = 8
            A = 2*pi / 5
            for n in range(5):
                bullet_pos = [radius*cos(n*A), radius*sin(n*A), pos[2]]
                self.bullets.append(Bullet(bullet_pos, BulletTypes(self.bullets_now)))
