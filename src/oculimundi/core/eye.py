# -*- coding: utf-8 -*-
"""
    This is the file of Eye class
"""

from oculimundi.core.entity import Entity

class Eye(Entity):
    
    def __init__(self, position):
        super().__init__(position, 0)
        self.health = 50

    def reset_position(self, position):
        self.position = position