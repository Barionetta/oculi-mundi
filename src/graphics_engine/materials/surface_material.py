# -*- coding: utf-8 -*-
"""
    This is the file of SurfaceMaterial class
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

from src.graphics_engine.materials.basic_material import BasicMaterial
from OpenGL.GL import *

class SurfaceMaterial(BasicMaterial):
    def __init__(self, properties={}):
        super().__init__()
        self.settings["draw_style"] = GL_TRIANGLES
        self.settings["double_side"] = False
        self.settings["wireframe"] = False
        self.settings["line_width"] = 1
        self.set_properties(properties)

    def update_render_settings(self):
        glLineWidth(self.settings["line_width"])
        if self.settings["double_side"]:
            glDisable(GL_CULL_FACE)
        else:
            glEnable(GL_CULL_FACE)

        if self.settings["wireframe"]:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        glLineWidth(self.settings["line_width"])