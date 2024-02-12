# -*- coding: utf-8 -*-
"""
    This is the file of Texture class
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

import pygame as pg
from OpenGL.GL import *

class Texture(object):

    def __init__(self, filename=None, properties={}):
        self.surface = None
        self.texture_ref = glGenTextures(1)
        self.properties = {
            "mag_filter": GL_LINEAR,
            "min_filter": GL_LINEAR_MIPMAP_LINEAR,
            "wrap"      : GL_REPEAT
        }
        self.set_properties(properties)
        if filename is not None:
            self.load_image(filename)
            self.upload_data()
    
    def load_image(self, filename):
        self.surface = pg.image.load(filename)
    
    def set_properties(self, props):
        for name, data in props.items():
            if name in self.properties.keys():
                self.properties[name] = data
            else:
                raise Exception("Texture has no property with name: " + name)
    
    def upload_data(self):
        width = self.surface.get_width()
        height = self.surface.get_height()
        pixel_data = pg.image.tostring(self.surface, "RGBA", True)
        glBindTexture(GL_TEXTURE_2D, self.texture_ref)
        glTexImage2D( GL_TEXTURE_2D, 0, GL_RGBA,
                     width, height, 0, GL_RGBA,
                     GL_UNSIGNED_BYTE, pixel_data)
        glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, self.properties["mag_filter"])
        glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, self.properties["min_filter"])
        glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, self.properties["wrap"])
        glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, self.properties["wrap"])
        glTexParameterfv( GL_TEXTURE_2D, GL_TEXTURE_BORDER_COLOR, [1,1,1,1])
        glGenerateMipmap(GL_TEXTURE_2D)
