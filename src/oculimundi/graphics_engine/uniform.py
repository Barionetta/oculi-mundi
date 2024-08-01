# -*- coding: utf-8 -*-
"""
    This is the file of Uniform class
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

from OpenGL.GL import *

class Uniform(object):
    
    def __init__(self, data_type, data):
        self.data_type = data_type
        self.data = data
        self.variable_ref = None
    
    def locate_variable(self, program_ref, variable_name):
        if self.data_type == "Light":
            self.variable_ref = {}
            self.variable_ref["light_type"] = glGetUniformLocation(program_ref, variable_name + ".light_type")
            self.variable_ref["color"] = glGetUniformLocation(program_ref, variable_name + ".color")
            self.variable_ref["direction"] = glGetUniformLocation(program_ref, variable_name + ".direction")
            self.variable_ref["position"] = glGetUniformLocation(program_ref, variable_name + ".position")
            self.variable_ref["attenuation"] = glGetUniformLocation(program_ref, variable_name + ".attenuation")
        else:
            self.variable_ref = glGetUniformLocation(program_ref, variable_name)
    
    def upload_data(self):
        if self.variable_ref == -1:
            return
        elif self.data_type == "int":
            glUniform1i(self.variable_ref, self.data)
        elif self.data_type == "bool":
            glUniform1i(self.variable_ref, self.data)
        elif self.data_type == "float":
            glUniform1f(self.variable_ref, self.data)
        elif self.data_type == "float":
            glUniform1f(self.variable_ref, self.data)
        elif self.data_type == "vec2":
            glUniform2f(self.variable_ref, self.data[0], self.data[1])
        elif self.data_type == "vec3":
            glUniform3f(self.variable_ref, self.data[0], self.data[1], self.data[2])
        elif self.data_type == "vec4":
            glUniform4f(self.variable_ref, self.data[0], self.data[1], self.data[2], self.data[3])
        elif self.data_type == "mat4":
            glUniformMatrix4fv(self.variable_ref, 1, GL_TRUE, self.data)
        elif self.data_type == "sampler2D":
            texture_object_ref, texture_unit_ref = self.data
            glActiveTexture( GL_TEXTURE0 + texture_unit_ref)
            glBindTexture( GL_TEXTURE_2D, texture_object_ref)
            glUniform1i( self.variable_ref, texture_unit_ref)
        elif self.data_type == "Light":
            glUniform1i( self.variable_ref["light_type"], self.data.light_type )
            glUniform3f( self.variable_ref["color"], self.data.color[0], self.data.color[1], self.data.color[2])
            direction = self.data.get_direction()
            glUniform3f( self.variable_ref["direction"], direction[0], direction[1], direction[2])
            position = self.data.get_position()
            glUniform3f( self.variable_ref["position"], position[0], position[1], position[2])
            glUniform3f( self.variable_ref["attenuation"], self.data.attenuation[0], self.data.attenuation[1],
                                                            self.data.attenuation[2])
