# -*- coding: utf-8 -*-
"""
    This is the file of RectangleGeometry and BoxGeometry class
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

import numpy as np
from src.graphics_engine.geometry.geometry import Geometry
from math import sin, cos, pi

class RectangleGeometry(Geometry):
    def __init__(self, width=1, height=1, position=[0,0], alignment=[0.5, 0.5]):
        super().__init__()

        x, y = position
        a, b = alignment
        P0 = [x + (-a)*width,  y + (-b)*height, 0]
        P1 = [x + (1-a)*width, y + (-b)*height, 0]
        P2 = [x + (-a)*width,  y + (1-b)*height, 0]
        P3 = [x + (1-a)*width, y + (1-b)*height, 0]
        C0, C1, C2, C3 = [1,1,1], [1,0,0], [0,1,0], [0,0,1]
        postion_data = [P0, P1, P3, P0, P3, P2]
        color_data = [C0, C1, C3, C0, C3, C2]
        
        T0, T1, T2, T3 = [0,0], [1,0], [0,1], [1,1]
        uvData = [T0, T1, T3, T0, T3, T2]

        normal_vector = [0,0,1]
        normal_data = [normal_vector] * 6

        self.add_attribute("vec3", "vertex_normal", normal_data)
        self.add_attribute("vec3", "face_normal", normal_data)
        self.add_attribute("vec2", "vertex_UV", uvData)
        self.add_attribute("vec3", "vertex_position", postion_data)
        self.add_attribute("vec3", "vertex_color", color_data)
        self.count_vertices()

class BoxGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        P0 = [-width/2, -height/2, -depth/2]
        P1 = [ width/2, -height/2, -depth/2]
        P2 = [-width/2,  height/2, -depth/2]
        P3 = [ width/2,  height/2, -depth/2]
        P4 = [-width/2, -height/2,  depth/2]
        P5 = [ width/2, -height/2,  depth/2]
        P6 = [-width/2,  height/2,  depth/2]
        P7 = [ width/2,  height/2,  depth/2]

        C1, C2 = [1, 0.5, 0.5], [0.5, 0, 0]
        C3, C4 = [0.5, 1, 0.5], [0, 0.5, 0]
        C5, C6 = [0.5, 0.5, 1], [0, 0, 0.5]
        postion_data = [ P5, P1, P3, P5, P3, P7,
                         P0, P4, P6, P0, P6, P2,
                         P6, P7, P3, P6, P3, P2,
                         P0, P1, P5, P0, P5, P4,
                         P4, P5, P7, P4, P7, P6,
                         P1, P0, P2, P1, P2, P3]
        
        color_data = [C1]*6 + [C2]*6 + [C3]*6 + [C4]*6 + [C5]*6 + [C6]*6

        T0, T1, T2, T3 = [0,0], [1,0], [0,1], [1,1]
        uvData = [T0, T1, T3, T0, T3, T2] * 6
        
        N1, N2 = [1,0,0], [-1, 0, 0]
        N3, N4 = [0,1,0], [0, -1, 0]
        N5, N6 = [0,0,1], [0, 0, -1]
        normal_data = [N1]*6 + [N2]*6 + [N3]*6 + [N4]*6 + [N5]*6 + [N6]*6

        self.add_attribute("vec3", "vertex_normal", normal_data)
        self.add_attribute("vec3", "face_normal", normal_data)
        self.add_attribute("vec2", "vertex_UV", uvData)
        self.add_attribute("vec3", "vertex_position", postion_data)
        self.add_attribute("vec3", "vertex_color", color_data)
        self.count_vertices()