# -*- coding: utf-8 -*-
"""
    This is the file of TextTexture class
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

import pygame as pg
from oculimundi.graphics_engine.texture import Texture

class TextTexture(Texture):
    
    def __init__(self, text="sample_text",
                        system_font_name="Arial",
                        font_file_name=None,
                        font_size=24,
                        font_color=(0,0,0),
                        background_color=(255,255,255),
                        transparent=False,
                        image_width=None,
                        image_height=None,
                        align_horizontal=0.0,
                        align_vertical=0.0,
                        image_border_width=0,
                        image_border_color=(0,0,0)):
        super().__init__()
        font = pg.font.SysFont(system_font_name, font_size)
        if font_file_name is not None:
            font = pg.font.Font(font_file_name, font_size)
        
        font_surface = font.render(text, True, font_color)
        (text_width, text_height) = font.size(text)

        if image_width is None:
            image_width = text_width
        if image_height is None:
            image_height = text_height
        self.surface = pg.Surface( ( image_width, image_height), pg.SRCALPHA)
        if not transparent:
            self.surface.fill( background_color )

        corner_point = (align_horizontal * (image_width - text_width), align_vertical * (image_height - text_height))
        destination_rectangle = font_surface.get_rect( topleft=corner_point )
        if image_border_width > 0:
            pg.draw.rect( self.surface, image_border_color, [0,0, image_width, image_height], image_border_width)
        self.surface.blit( font_surface, destination_rectangle)
        self.upload_data()