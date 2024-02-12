# -*- coding: utf-8 -*-
"""
    This is the file of Mesh class
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

from src.graphics_engine.object3D import Object3D
from OpenGL.GL import *

class Mesh(Object3D):

    def __init__(self, geometry, material):
        super().__init__()
        self.geometry = geometry
        self.material = material
        self.is_visible = True
        self.VAO = glGenVertexArrays(1)
        glBindVertexArray(self.VAO)
        for variable_name, attribute_object in geometry.attributes.items():
            attribute_object.associate_variable(material.program_ref, variable_name)
        glBindVertexArray(0)