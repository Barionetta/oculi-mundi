# -*- coding: utf-8 -*-
"""
    This is the file of MovementRig class
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

from src.graphics_engine.object3D import Object3D

class MovementRig(Object3D):

    def __init__(self, degrees_per_second=60):
        super().__init__()
        self.look_attachment = Object3D()
        self.children = [self.look_attachment]
        self.look_attachment.parent = self
        self.degrees_per_second = degrees_per_second

        ''' KEYS '''
        self.KEY_TURN_LEFT = "right"
        self.KEY_TURN_RIGHT = "left"
        self.KEY_LOOK_UP = "down"
        self.KEY_LOOK_DOWN = "up"
    
    def add(self, child):
        self.look_attachment.add(child)
    
    def remove(self, child):
        self.look_attachment.remove(child)

    def update(self, input_object, delta_time):

        rotate_amount =  self.degrees_per_second * (3.1415926 / 180) * delta_time

        if input_object.is_key_pressed(self.KEY_TURN_RIGHT):
            self.rotateY(-rotate_amount)
        if input_object.is_key_pressed(self.KEY_TURN_LEFT):
            self.rotateY(rotate_amount)
        if input_object.is_key_pressed(self.KEY_LOOK_UP):
            self.rotateX(rotate_amount)
        if input_object.is_key_pressed(self.KEY_LOOK_DOWN):
            self.rotateX(-rotate_amount)