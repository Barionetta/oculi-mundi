# -*- coding: utf-8 -*-
"""
    This is the file of BasicMaterial class
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

from src.graphics_engine.materials.material import Material
from OpenGL.GL import *

class BasicMaterial(Material):
    def __init__(self):

        with open("src/graphics_engine/shaders/point_vertex.txt", 'r') as f:
            vertex_shader_code = f.readlines()
        with open("src/graphics_engine/shaders/point_fragment.txt", 'r') as f:
            fragment_shader_code = f.readlines()

        vertex_shader_code = "\n".join(vertex_shader_code)
        fragment_shader_code = "\n".join(fragment_shader_code)
        super().__init__(vertex_shader_code, fragment_shader_code)
        self.add_uniform("vec3", "base_color", [1.0, 1.0, 1.0])
        self.add_uniform("bool", "use_vertex_color", False)
        self.locate_uniforms()

class PointMaterial(BasicMaterial):
    def __init__(self, properties={}):
        super().__init__()
        self.settings["draw_style"] = GL_POINTS
        self.settings["point_size"] = 2
        self.settings["rounded_points"] = False
        self.set_properties(properties)

    def update_render_settings(self):
        glPointSize(self.settings["point_size"])
        if self.settings["rounded_points"]:
            glEnable(GL_POINT_SMOOTH)
        else:
            glDisable(GL_POINT_SMOOTH)