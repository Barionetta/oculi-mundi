# -*- coding: utf-8 -*-
"""
    This is the file of TextureMaterial class
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

from OpenGL.GL import *
from src.graphics_engine.materials.material import Material

class TextureMaterial(Material):

    def __init__(self, texture, properties={}):
        
        with open("src/graphics_engine/shaders/tex_vertex.txt", 'r') as f:
            vertex_shader_code = f.readlines()
        with open("src/graphics_engine/shaders/tex_fragment.txt", 'r') as f:
            fragment_shader_code = f.readlines()
        vertex_shader_code = "\n".join(vertex_shader_code)
        fragment_shader_code = "\n".join(fragment_shader_code)
        
        super().__init__(vertex_shader_code, fragment_shader_code)
        self.add_uniform("vec3", "base_color", [1.0, 1.0, 1.0])
        self.add_uniform("sampler2D", "texture_sampler", [texture.texture_ref, 1])
        self.add_uniform("vec2", "repeat_UV", [1.0, 1.0])
        self.add_uniform("vec2", "offset_UV", [0.0, 0.0])
        self.locate_uniforms()
        
        self.settings["double_side"] = True
        self.settings["wireframe"] = False
        self.settings["line_width"] = 1
        self.set_properties(properties)

    def update_render_settings(self):
        if self.settings["double_side"]:
            glDisable(GL_CULL_FACE)
        else:
            glEnable(GL_CULL_FACE)

        if self.settings["wireframe"]:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glLineWidth(self.settings["line_width"])