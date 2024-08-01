# -*- coding: utf-8 -*-
"""
    This is the file of Material class
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

from OpenGL.GL import *
from oculimundi.graphics_engine.utils import OpenGLUtils
from oculimundi.graphics_engine.uniform import Uniform

class Material(object):

    def __init__(self, vertex_shader_code, fragment_shader_code):
        self.program_ref = OpenGLUtils.starup_program( vertex_shader_code, fragment_shader_code)
        self.uniforms = {}
        self.uniforms["model_matrix"] = Uniform("mat4", None)
        self.uniforms["view_matrix"] = Uniform("mat4", None)
        self.uniforms["projection_matrix"] = Uniform("mat4", None)
        self.settings = {}
        self.settings["draw_style"] = GL_TRIANGLES
    
    def add_uniform(self, data_type, variable_name, data):
        self.uniforms[variable_name] = Uniform(data_type, data)
    
    def locate_uniforms(self):
        for variable_name, uniform_object in self.uniforms.items():
            uniform_object.locate_variable( self.program_ref, variable_name )
    
    def update_render_settings(self):
        pass

    def set_properties(self, properties):
        for name, data in properties.items():
            if name in self.uniforms.keys():
                self.uniforms[name].data = data
            elif name in self.settings.keys():
                self.settings[name] = data
            else:
                raise Exception( "Material has no property named: " + name)
