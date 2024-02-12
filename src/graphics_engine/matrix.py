# -*- coding: utf-8 -*-
"""
    This is the file of Matrix class
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

import numpy as np
from math import sin, cos, tan, pi
from numpy import subtract, divide, cross
from numpy.linalg import norm

class Matrix(object):

    @staticmethod
    def makeIdentity():
        return np.array( [[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]]).astype(float)
    
    @staticmethod
    def makeTranslation(x, y, z):
        return np.array( [[1, 0, 0, x],
                          [0, 1, 0, y],
                          [0, 0, 1, z],
                          [0, 0, 0, 1]]).astype(float)
    
    @staticmethod
    def makeRotationX(angle):
        c = cos(angle)
        s = sin(angle)
        return np.array( [[1, 0, 0, 0],
                          [0, c, -s, 0],
                          [0, s, c, 0],
                          [0, 0, 0, 1]]).astype(float)
    
    @staticmethod
    def makeRotationY(angle):
        c = cos(angle)
        s = sin(angle)
        return np.array( [[c, 0, s, 0],
                          [0, 1, 0, 0],
                          [-s, 0, c, 0],
                          [0, 0, 0, 1]]).astype(float)
    
    @staticmethod
    def makeRotationZ(angle):
        c = cos(angle)
        s = sin(angle)
        return np.array( [[c, -s, 0, 0],
                          [s, c, 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]]).astype(float)
    
    @staticmethod
    def makeScale(s):
        return np.array( [[s, 0, 0, 0],
                          [0, s, 0, 0],
                          [0, 0, s, 0],
                          [0, 0, 0, 1]]).astype(float)
    
    @staticmethod
    def make_look_at(position, target):
        world_up = [0, 1, 0]
        forward = subtract(target, position)
        right = cross(forward, world_up)

        if norm(right) < 0.001:
            offset = np.array( [0.001, 0, 0])
            right = cross( forward, world_up + offset)
        up = cross( right, forward)

        forward = divide(forward, norm(forward))
        right = divide( right, norm(right))
        up = divide( up, norm(up))

        return np.array( [[right[0], up[0], -forward[0], position[0]],
                         [right[1], up[1], -forward[1], position[1]],
                         [right[2], up[2], -forward[2], position[2]],
                         [0, 0, 0, 1]])

    @staticmethod
    def makePerspective(angle_of_view=60, aspect_ratio=1, near=0.1, far=1000):
        a = angle_of_view * pi / 180.0
        d = 1.0 / tan(a/2)
        r = aspect_ratio
        b = (far + near) / (near - far)
        c = 2 * far * near / (near - far)
        return np.array( [[d/r, 0, 0, 0],
                          [0, d, 0, 0],
                          [0, 0, b, c],
                          [0, 0, -1, 0]]).astype(float)
    
    @staticmethod
    def makeOrtographic(left=-1, right=1, bottom=-1,top=1, near=-1, far=1):
        return np.array( [[2/(right-left), 0, 0, -(right+left)/(right-left)],
                          [0, 2/(top-bottom), 0, -(top+bottom)/(top-bottom)],
                          [0, 0, -2/(far-near), -(far+near)/(far-near)],
                          [0, 0, 0, 1]]).astype(float)
