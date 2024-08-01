# -*- coding: utf-8 -*-
"""
    This is the file of Entity class
"""

import numpy as np

class Entity(object):
    
    def __init__(self, position, velocity):
        self.position = np.array(position, dtype=float)
        self.velocity = velocity

    def is_colliding(self, obj, dist):
        distance = abs(np.subtract(self.position, obj.position))
        if (distance[0] < dist and distance[1] < dist) and distance[2] < dist:
            return True
    
    def update(self):
        pass

