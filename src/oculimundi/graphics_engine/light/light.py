# -*- coding: utf-8 -*-
"""
    This is the file of Light class and its children
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

from oculimundi.graphics_engine.object3D.object3D import Object3D

class Light(Object3D):
    
    AMBIENT = 1
    DIRECTIONAL = 2
    POINT = 3

    def __init__(self, ligth_type=0):
        super().__init__()
        self.light_type = ligth_type
        self.color = [1,1,1]
        self.attenuation = [1,0,0]

class AmbientLight(Light):
    
    def __init__(self, color=[1,1,1]):
        super().__init__(Light.AMBIENT)
        self.color = color

class DirectionalLight(Light):
    
    def __init__(self, color=[1,1,1], direction=[0,-1,0]):
        super().__init__(Light.DIRECTIONAL)
        self.color = color
        self.set_direction( direction )

class PointLight(Light):
    
    def __init__(self, color=[1,1,1], position=[0,0,0], attenuation=[1,0,0.1]):
        super().__init__(Light.POINT)
        self.color = color
        self.set_position( position )
        self.attentuation = attenuation