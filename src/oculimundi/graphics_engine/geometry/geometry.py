# -*- coding: utf-8 -*-
"""
    This is the file of Geometry class
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

import numpy as np
from oculimundi.graphics_engine.attribute import Attribute

class Geometry(object):

    def __init__(self):
        self.attributes = {}
        self.vertex_count = None
    
    def add_attribute(self, data_type, variable_name, data):
        self.attributes[variable_name] = Attribute(data_type, data)
    
    def count_vertices(self):
        attrib = list( self.attributes.values())[0]
        self.vertex_count = len(attrib.data)

    def apply_matrix(self, matrix, variable_name="vertex_position"):
        old_position_data = self.attributes[variable_name].data
        new_position_data = []

        for old_position in old_position_data:
            new_position = old_position.copy()
            new_position.append(1)
            new_position = matrix @ new_position
            new_position = list(new_position[0:3])
            new_position_data.append(new_position)
        
        self.attributes[variable_name].data = new_position_data
        self.attributes[variable_name].upload_data()

        rotation_matrix = np.array([matrix[0][0:3],
                                    matrix[1][0:3],
                                    matrix[2][0:3]])
        
        old_vertex_normal_data = self.attributes["vertex_normal"].data
        new_vertex_normal_data = []
        for old_normal in old_vertex_normal_data:
            new_normal = old_normal.copy()
            new_normal = rotation_matrix @ new_normal
            new_vertex_normal_data.append( new_normal )
        self.attributes["vertex_normal"].data = new_vertex_normal_data

        old_face_normal_data = self.attributes["face_normal"].data
        new_face_normal_data = []
        for old_normal in old_face_normal_data:
            new_normal = old_normal.copy()
            new_normal = rotation_matrix @ new_normal
            new_face_normal_data.append( new_normal )
        self.attributes["face_normal"].data = new_face_normal_data

    def merge(self, other_geometry):
        for variable_name, attribute_object in self.attributes.items():
            attribute_object.data += other_geometry.attributes[variable_name].data
            attribute_object.upload_data()
        self.count_vertices()