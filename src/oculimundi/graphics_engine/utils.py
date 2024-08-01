# -*- coding: utf-8 -*-
"""
    This is the file of utils functions
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

from OpenGL.GL import *

class OpenGLUtils(object):

    @staticmethod
    def initialize_shader(shader_code, shader_type):
        shader_code = "#version 330\n" + shader_code
        shader_ref = glCreateShader(shader_type)
        glShaderSource(shader_ref, shader_code)
        glCompileShader(shader_ref)
        compile_success = glGetShaderiv(shader_ref, GL_COMPILE_STATUS)
        if not compile_success:
            error_message = glGetShaderInfoLog(shader_ref)
            glDeleteShader(shader_ref)
            error_message = '\n' + error_message.decode('utf-8')
            raise Exception( error_message )
        return shader_ref
    
    @staticmethod
    def print_system_info():
        print("Vendor: " + glGetString(GL_VENDOR).decode('utf-8'))
        print("Renderer: " + glGetString(GL_RENDERER).decode('utf-8'))
        print("OpenGL version supported: " + glGetString(GL_VERSION).decode('utf-8'))
    
    @staticmethod
    def starup_program(vertex_shader_code, fragment_shader_code):
        vertex_shader_ref = OpenGLUtils.initialize_shader( vertex_shader_code, GL_VERTEX_SHADER)
        fragment_shader_ref = OpenGLUtils.initialize_shader( fragment_shader_code, GL_FRAGMENT_SHADER)
        program_ref = glCreateProgram()
        glAttachShader(program_ref, vertex_shader_ref)
        glAttachShader(program_ref, fragment_shader_ref)
        glLinkProgram(program_ref)
        link_success = glGetProgramiv(program_ref, GL_LINK_STATUS)
        if not link_success:
            error_message = glGetShaderInfoLog(program_ref)
            glDeleteProgram(program_ref)
            error_message = '\n' + error_message.decode('utf-8')
            raise Exception( error_message )
        return program_ref
