# -*- coding: utf-8 -*-
"""
    This is the file of Test class
"""
__version__ = '0.1.0'
__author__ = 'Katarzyna Matuszek'

import pygame
import sys
from src.graphics_engine.renderer import Renderer
from src.graphics_engine.object3D.scene import Scene, Group
from src.graphics_engine.object3D.camera import Camera
from src.graphics_engine.object3D.mesh import Mesh
#from src.graphics_engine.light.light import AmbientLight, DirectionalLight, PointLight
from src.graphics_engine.geometry.parametric_geometry import EllipsoidGeometry, SphereGeometry, CylinderGeometry
from src.graphics_engine.geometry.rectangle_geometry import BoxGeometry, RectangleGeometry
from src.graphics_engine.object3D.movement_rig import MovementRig
from src.graphics_engine.texture import Texture
#from src.graphics_engine.text_texture import TextTexture
from src.graphics_engine.materials.basic_material import BasicMaterial
from src.graphics_engine.materials.point_material import PointMaterial
from src.graphics_engine.materials.texture_material import TextureMaterial
from src.input import Input

class Test:

    def __init__(self, screen_size=[800,600]):
        pygame.init()
        display_flags = pygame.DOUBLEBUF | pygame.OPENGL
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        self.screen = pygame.display.set_mode(screen_size, display_flags)
        pygame.display.set_caption("Test")
        self.running = True
        self.clock = pygame.time.Clock()
        self.time = 0
        self.delta_time = 0
        self.speed = 0.5
        self.input = Input()

    def startup(self):
        print("To jest test")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera( aspect_ratio=800/600)
        self.rig = MovementRig()
        self.rig.add( self.camera )
        self.rig.set_position( [0,0,0])
        self.scene.add(self.rig)

        material = BasicMaterial()
        wings = Mesh(RectangleGeometry(9, 2), material)
        wings.rotateX(3.14 / 2)
        wings.set_position([0,-5,-20])
        shipbase = Mesh(CylinderGeometry(1, 5), material)
        shipbase.set_position([0,-5,-20])
        shipbase.rotateX(3.14 / 2)
        self.spaceship = Group()
        self.spaceship.add(shipbase)
        self.spaceship.add(wings)
        self.scene.add(self.spaceship)
        '''
        skyGeometry = CylinderGeometry(60, 80)
        skyMaterial = TextureMaterial( Texture("graphics_engine/textures/skybox.png"))
        self.sky = Mesh( skyGeometry, skyMaterial )
        self.sky.rotateX(3.14 / 2)
        self.scene.add(self.sky)
        '''
        skyGeometry = SphereGeometry(radius=30)
        skyMaterial = PointMaterial()
        self.sky = Mesh( skyGeometry, skyMaterial )
        self.sky.set_position([0, 0, -10])
        self.sky.rotateX(3.14 / 2)
        self.scene.add(self.sky)

        eyeGeometry = SphereGeometry(radius=8, radius_segments=256, height_segments=128)
        eyeMaterial = TextureMaterial( Texture("graphics_engine/textures/eye.png"))
        eye = Mesh( eyeGeometry, eyeMaterial )
        eye.set_position([0, 5, -30])
        eye.rotateY(3.14)
        self.scene.add(eye)

    def update(self):
        self.sky.rotateY(0.02)
        self.sky.rotateX(0.05)
        self.sky.rotateZ(0.05)
        self.rig.update(self.input, self.delta_time)
        self.renderer.render(self.scene, self.camera)

    def run(self):
        self.startup()
        while self.running:
            self.update()
            self.input.update()
            if self.input.quit:
                self.running = False
            pygame.display.flip()
            self.clock.tick(60)
            self.delta_time = self.clock.get_time() / 1000
            self.time += self.delta_time
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Test(screen_size=[800,600]).run()