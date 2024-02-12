# -*- coding: utf-8 -*-
"""
    This is the file of Object3D class
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

import numpy
from src.graphics_engine.matrix import Matrix

class Object3D(object):

    def __init__(self):
        self.transform = Matrix.makeIdentity()
        self.parent = None
        self.children = []
    
    def add(self, child):
        self.children.append(child)
        child.parent = self
    
    def remove(self, child):
        self.children.remove(child)
        child.parent = None

    def look_at(self, target_position):
        self.transform = Matrix.make_look_at( self.get_world_position(), target_position)

    def get_world_matrix(self):
        if self.parent == None:
            return self.transform
        else:
            return self.parent.get_world_matrix() @ self.transform

    def get_descendant_list(self):
        descendants = []
        nodes_to_process = [self]
        while len(nodes_to_process) > 0:
            node = nodes_to_process.pop(0)
            descendants.append(node)
            nodes_to_process = node.children + nodes_to_process
        return descendants
    
    ''' Matrix Functions '''

    def apply_matrix(self, matrix, localCoord=True):
        if localCoord:
            self.transform = self.transform @ matrix
        else:
            self.transform = matrix @ self.transform

    def translate(self, x, y, z, localCoord=True):
        m = Matrix.makeTranslation(x, y, z)
        self.apply_matrix(m, localCoord)
    
    def rotateX(self, angle, localCoord=True):
        m = Matrix.makeRotationX(angle)
        self.apply_matrix(m, localCoord)
    
    def rotateY(self, angle, localCoord=True):
        m = Matrix.makeRotationY(angle)
        self.apply_matrix(m, localCoord)

    def rotateZ(self, angle, localCoord=True):
        m = Matrix.makeRotationZ(angle)
        self.apply_matrix(m, localCoord)

    def scale(self, s, localCoord=True):
        m = Matrix.makeScale(s)
        self.apply_matrix(m, localCoord)

    ''' Positions '''

    def get_position(self):
        return [self.transform.item((0,3)),
                self.transform.item((1,3)),
                self.transform.item((2,3))]
    
    def get_world_position(self):
        world_transform = self.get_world_matrix()
        return [world_transform.item((0,3)),
                world_transform.item((1,3)),
                world_transform.item((2,3))]
    
    def set_position(self, position):
        self.transform.itemset((0, 3), position[0])
        self.transform.itemset((1, 3), position[1])
        self.transform.itemset((2, 3), position[2])
    
    ''' Rotation Data '''
    def get_rotation_matrix(self):
        return [self.transform[0][0:3],
                self.transform[1][0:3],
                self.transform[2][0:3]]
    
    def get_direction(self):
        forward = numpy.array([0,0,-1])
        return list(self.get_rotation_matrix() @ forward)
    
    def set_direction(self, direction):
        position = self.get_position()
        target_position = [ position[0] + direction[0],
                            position[1] + direction[1],
                            position[2] + direction[2],]
        self.look_at(target_position)