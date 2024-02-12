# -*- coding: utf-8 -*-
"""
    This is the file of Camera class
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

from src.graphics_engine.object3D.object3D import Object3D
from src.graphics_engine.matrix import Matrix
from numpy.linalg import inv

class Camera(Object3D):

    def __init__(self, angle_of_view=60, aspect_ratio=1, near=0.1, far=1000):
        super().__init__()
        self.projection_matrix = Matrix.makePerspective(angle_of_view, aspect_ratio, near, far)
        self.view_matrix = Matrix.makeIdentity()
    
    def update_view_matrix(self):
        self.view_matrix = inv( self.get_world_matrix())

    def set_perspective(self, angle_of_view=50, aspect_ratio=1, near=0.1, far=1000):
        self.projection_matrix = Matrix.makePerspective( angle_of_view, aspect_ratio, near, far)

    def set_ortographic(self, left=-1, right=1, bottom=-1,top=1, near=-1, far=1):
        self.projection_matrix = Matrix.makeOrtographic(left, right, bottom, top, near, far) 