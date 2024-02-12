# -*- coding: utf-8 -*-
"""
    This is the file of FlatMaterial class
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

from OpenGL.GL import *
from src.graphics_engine.materials.material import Material

class PhongMaterial(Material):

    def __init__(self, texture=None, properties={}):

        with open("src/graphics_engine/shaders/phong_vertex.txt", 'r') as f:
            vertex_shader_code = f.readlines()
        with open("src/graphics_engine/shaders/phong_fragment.txt", 'r') as f:
            fragment_shader_code = f.readlines()
        vertex_shader_code = "\n".join(vertex_shader_code)
        fragment_shader_code = "\n".join(fragment_shader_code)

        super().__init__(vertex_shader_code, fragment_shader_code)
        self.add_uniform("vec3", "base_color", [1.0, 1.0, 1.0])

        self.add_uniform("vec3", "view_position", [0,0,0])
        self.add_uniform("float", "specular_strength", 1)
        self.add_uniform("float", "shininess", 32)

        self.add_uniform("Light", "light0", None)
        self.add_uniform("Light", "light1", None)
        self.add_uniform("Light", "light2", None)
        self.add_uniform("Light", "light3", None)
        self.add_uniform("bool", "use_texture", 0)

        if texture == None:
            self.add_uniform("bool", "use_texture", False)
        else:
            self.add_uniform("bool", "use_texture", True)
            self.add_uniform("sampler2D", "texture", [texture.texture_ref, 1])

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