# -*- coding: utf-8 -*-
"""
    This is the file of Scene and Group classes
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

from src.graphics_engine.object3D.object3D import Object3D

class Scene(Object3D):

    def __init__(self):
        super().__init__()


class Group(Object3D):

    def __init__(self):
        super().__init__()