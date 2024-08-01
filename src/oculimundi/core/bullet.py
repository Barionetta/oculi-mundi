# -*- coding: utf-8 -*-
"""
    This is the file of Bullet class
"""

from enum import Enum
import numpy as np
from oculimundi.core.entity import Entity

class BulletTypes(Enum):
    FLOWER = 1
    RAY = 2
    RINGS = 3
    PLAYER = 4

class Bullet(Entity):

    def __init__(self, position, type):
        super().__init__(position, 0.2)
        self.type = type
        self.has_hit = False
        self.mesh = None
        self.radius = 0.6
        if type == BulletTypes.PLAYER:
            self.radius = 2
            self.velocity = 3
        if type == BulletTypes.RAY or BulletTypes.RINGS:
            self.radius = 0.8
            self.velocity = 0.6

    def update(self):
        if self.type == BulletTypes.RAY:
            self.ray_pattern()
        if self.type == BulletTypes.FLOWER:
            self.flower_pattern()
        if self.type == BulletTypes.RINGS:
            self.rings_pattern()
            self.velocity = 0.6
        if self.type == BulletTypes.PLAYER:
            self.player_pattern()

    def ray_pattern(self):
        old_x = self.position[0]
        old_y = self.position[1]
        self.position[0] = -0.03 * old_x + old_x
        self.position[1] = 0.03 * old_y + old_y
        self.position[2] += self.velocity

    def flower_pattern(self):
        old_x = self.position[0]
        old_y = self.position[1]
        self.position[0] = -0.04 * old_y + old_x
        self.position[1] = 0.04 * old_x + old_y
        self.position[2] += self.velocity

    def rings_pattern(self):
        old_x = self.position[0]
        old_y = self.position[1]
        self.position[0] = -0.03 * old_y + old_x
        self.position[1] = -0.03 * old_x + old_y
        self.position[2] += self.velocity

    def player_pattern(self):
        self.position[2] -= self.velocity