# -*- coding: utf-8 -*-
"""
    This is the file of Eye class
"""
__version__ = '0.1.0'
__author__ = 'Katarzyna Matuszek'

from src.core.entity import Entity

class Eye(Entity):
    
    def __init__(self, position):
        super().__init__(position, 0)
        self.health = 50

    def reset_position(self, position):
        self.position = position