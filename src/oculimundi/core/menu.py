# -*- coding: utf-8 -*-
"""
    This is the file of Menu class
"""

import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Menu:

    def __init__(self):

        # 1 - start/restart 0 - quit
        self.choice = -1
        self.focus = 1
        
        ''' KEYS '''
        self.KEY_MOVE_UP = "up"
        self.KEY_MOVE_DOWN = "down"
        self.CONFIRM = "return"

    def update(self, input_object):

        if input_object.is_key_pressed(self.KEY_MOVE_UP):
            self.focus = 1
        if input_object.is_key_pressed(self.KEY_MOVE_DOWN):
            self.focus = 0
        if input_object.is_key_pressed(self.CONFIRM):
            if self.focus == 1:
                self.choice = 1
            else:
                self.choice = 0
    
    def reset_choice(self):
        self.choice = 1
