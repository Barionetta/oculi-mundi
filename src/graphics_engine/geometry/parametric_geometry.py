# -*- coding: utf-8 -*-
"""
    This is the file of ParametricGeometry class and its children
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

import numpy as np
from src.graphics_engine.geometry.geometry import Geometry
from src.graphics_engine.geometry.polygon_geometry import PolygonGeometry
from src.graphics_engine.matrix import Matrix
from math import sin, cos, pi

class ParametricGeometry(Geometry):

    def __init__(self, uStart, uEnd, uResolution, vStart, vEnd, vResolution, surface_function):

        super().__init__()
        deltaU = (uEnd - uStart) / uResolution
        deltaV = (vEnd - vStart) / vResolution
        positions = []
        
        for uIndex in range(uResolution + 1):
            vArray = []
            for vIndex in range(vResolution + 1):
                u = uStart + uIndex * deltaU
                v = vStart + vIndex * deltaV
                vArray.append( surface_function(u, v))
            positions.append(vArray)
        
        position_data = []
        color_data = []
        C1, C2, C3 = [1,0,0], [0,1,0], [0,0,1]
        C4, C5, C6 = [0,1,1], [1,0,1], [1,1,0]

        uvs = []
        uv_data = []
        for uIndex in range(uResolution + 1):
            vArray = []
            for vIndex in range(vResolution + 1):
                u = uIndex/uResolution
                v = vIndex/vResolution
                vArray.append( [u, v])
            uvs.append(vArray)

        def calc_normal(P0, P1, P2):
            v1 = np.array(P1) - np.array(P0)
            v2 = np.array(P2) - np.array(P0)
            orthogonal_vector = np.cross( v1, v2)
            norm = np.linalg.norm(orthogonal_vector)
            normal = orthogonal_vector / norm if norm > 1e-6 \
                        else np.array(P0) / np.linalg.norm(P0)
            return normal
        
        vertex_normals = []
        for uIndex in range(uResolution + 1):
            vArray = []
            for vIndex in range(vResolution + 1):
                u = uStart + uIndex * deltaU
                v = vStart + vIndex * deltaV
                h = 0.0001
                P0 = surface_function(u, v)
                P1 = surface_function(u+h, v)
                P2 = surface_function(u, v+h)
                normal_vector = calc_normal(P0, P1, P2)
                vArray.append( normal_vector )
            vertex_normals.append(vArray)

        vertex_normal_data = []
        face_normal_data = []

        for xIndex in range(uResolution):
            for yIndex in range(vResolution):
                pA = positions[xIndex+0][yIndex+0]
                pB = positions[xIndex+1][yIndex+0]
                pC = positions[xIndex+1][yIndex+1]
                pD = positions[xIndex+0][yIndex+1]
                position_data += [pA.copy(), pB.copy(), pC.copy(), pA.copy(), pC.copy(), pD.copy()]
                color_data += [C1, C2, C3, C4, C5, C6]

                uvA = uvs[xIndex+0][yIndex+0]
                uvB = uvs[xIndex+1][yIndex+0]
                uvC = uvs[xIndex+0][yIndex+1]
                uvD = uvs[xIndex+1][yIndex+1]
                uv_data += [uvA, uvB, uvC, uvA, uvC, uvD]

                nA = vertex_normals[xIndex+0][yIndex+0]
                nB = vertex_normals[xIndex+1][yIndex+0]
                nC = vertex_normals[xIndex+0][yIndex+1]
                nD = vertex_normals[xIndex+1][yIndex+1]
                vertex_normal_data += [nA, nB, nC, nA, nC, nD]

                fn0 = calc_normal(pA, pB, pC)
                fn1 = calc_normal(pA, pC, pD)
                face_normal_data += [fn0, fn0, fn0, fn1, fn1, fn1]

        self.add_attribute("vec3", "vertex_normal", vertex_normal_data)
        self.add_attribute("vec3", "face_normal", face_normal_data)
        self.add_attribute("vec3", "vertex_position", position_data)
        self.add_attribute("vec3", "vertex_color", color_data)
        self.add_attribute("vec2", "vertex_UV", uv_data)
        self.count_vertices()


class EllipsoidGeometry(ParametricGeometry):

    def __init__(self, width=1, height=1, depth=1, radius_segments=32, height_segments=16):

        def S(u,v):
            return [ width/2 * sin(u) * cos(v),
                     height/2 * sin(v)        ,
                     depth/2 * cos(u) * cos(v)]
        
        super().__init__(0, 2*pi, radius_segments, -pi/2, pi/2, height_segments, S)

class SphereGeometry(EllipsoidGeometry):

    def __init__(self, radius=1, radius_segments=32, height_segments=16):
        super().__init__(2*radius, 2*radius, 2*radius, radius_segments, height_segments)

class CylindricalGeometry(ParametricGeometry):

    def __init__(self, radius_top=1, radius_bottom=1, height=1, radial_segments=32,
                 height_segments=4, closed_top=True, closed_bottom=True):

        def S(u,v):
            return [ (v * radius_top + (1-v) * radius_bottom) * sin(u),
                     height * (v - 0.5),
                     (v * radius_top + (1-v) * radius_bottom) * cos(u)]
        
        super().__init__(0, 2*pi, radial_segments, 0, 1, height_segments, S)

        if closed_top:
            top_geometry = PolygonGeometry( radial_segments, radius_top)
            transform = Matrix.makeTranslation(0, height/2, 0) @ Matrix.makeRotationY(-pi/2) @ Matrix.makeRotationX(-pi/2)
            top_geometry.apply_matrix( transform )
            self.merge( top_geometry )

        if closed_bottom:
            bottom_geometry = PolygonGeometry( radial_segments, radius_top)
            transform = Matrix.makeTranslation(0, -height/2, 0) @ Matrix.makeRotationY(-pi/2) @ Matrix.makeRotationX(pi/2)
            bottom_geometry.apply_matrix( transform )
            self.merge( bottom_geometry )


class CylinderGeometry(CylindricalGeometry):
    def __init__(self, radius=1, height=1, radial_segments=32, height_segments=4, closed=True):
        super().__init__(radius, radius, height, radial_segments, height_segments, closed, closed)