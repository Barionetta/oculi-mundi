# -*- coding: utf-8 -*-
"""
    This is the file of Spaceship class
"""
__version__ = '0.1.0'
__author__ = 'Katarzyna Matuszek'

from src.core.entity import Entity

class Spaceship(Entity):
    
    def __init__(self, position):
        super().__init__(position, 12)
        self.health = 20

        ''' MOVEMENT KEYS '''
        self.KEY_MOVE_LEFT = "a"
        self.KEY_MOVE_RIGHT = "d"
        self.KEY_MOVE_UP = "w"
        self.KEY_MOVE_DOWN = "s"
    
    def update(self, input_object, delta_time):

        move_amount = self.velocity * delta_time

        if input_object.is_key_pressed(self.KEY_MOVE_LEFT):
            self.position[0] -= move_amount
        if input_object.is_key_pressed(self.KEY_MOVE_RIGHT):
            self.position[0] += move_amount
        if input_object.is_key_pressed(self.KEY_MOVE_UP):
            self.position[1] += move_amount
        if input_object.is_key_pressed(self.KEY_MOVE_DOWN):
            self.position[1] -= move_amount
        self.reset_position()

    def reset_position(self):
        if self.position[0] < -34 or self.position[0] > 34:
            self.position[0] = 0
        if self.position[1] < -21 or self.position[1] > 21:
            self.position[1] = 0