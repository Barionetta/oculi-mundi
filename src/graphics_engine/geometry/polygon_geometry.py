# -*- coding: utf-8 -*-
"""
    This is the file of PolygonGeometry class
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

from src.graphics_engine.geometry.geometry import Geometry
from math import sin, cos, pi

class PolygonGeometry(Geometry):

    def __init__(self, sides=3, radius=1):
        super().__init__()

        A = 2*pi / sides
        position_data = []
        color_data = []
        uv_data = []
        uv_center = [0.5, 0.5]
        vertex_normal_data = []
        normal_vector = [0, 0, 1]

        for n in range(sides):
            position_data.append([0, 0, 0])
            position_data.append([ radius*cos(n*A), radius*sin(n*A), 0])
            position_data.append([ radius*cos((n+1)*A), radius*sin((n+1)*A), 0])
            color_data.append( [1, 1, 1])
            color_data.append( [1, 0, 0])
            color_data.append( [0, 0, 1])
            uv_data.append( uv_center )
            uv_data.append( [cos(n*A)*0.5 + 0.5, sin(n*A)*0.5 + 0.5])
            uv_data.append( [cos((n+1)*A)*0.5 + 0.5, sin((n+1)*A)*0.5 + 0.5])

            for _ in range(3):
                vertex_normal_data.append(normal_vector.copy())
        
        self.add_attribute("vec3", "vertex_position", position_data)
        self.add_attribute("vec3", "vertex_color", color_data)
        self.add_attribute("vec3", "vertex_normal", vertex_normal_data)
        self.add_attribute("vec3", "face_normal", vertex_normal_data)
        self.add_attribute("vec2", "vertex_UV", uv_data)
        self.count_vertices()