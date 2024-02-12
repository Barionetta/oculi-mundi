# -*- coding: utf-8 -*-
"""
    This is the file of Matrix class
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

import pygame as pg

class Input(object):

    def __init__(self):
        self.quit = False
        self.key_down_list = []
        self.key_pressed_list = []
        self.key_up_list = []
    
    def update(self):

        self.key_down_list = []
        self.key_up_list = []

        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.quit = True

            if event.type == pg.KEYDOWN:
                key_name = pg.key.name( event.key )
                self.key_down_list.append( key_name )
                self.key_pressed_list.append( key_name )

            if event.type == pg.KEYUP:
                key_name = pg.key.name( event.key )
                self.key_pressed_list.remove( key_name )
                self.key_up_list.append( key_name )
    
    def is_key_down(self, key_code):
        return key_code in self.key_down_list
    
    def is_key_pressed(self, key_code):
        return key_code in self.key_pressed_list
    
    def is_key_up(self, key_code):
        return key_code in self.key_up_list