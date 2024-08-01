# -*- coding: utf-8 -*-
"""
    This is the file of Game class
"""

# Libraries
import pygame as pg
from enum import Enum
import sys
# Input
from oculimundi.input import Input
# Core
from oculimundi.core.level import Level
from oculimundi.core.bullet import BulletTypes
from oculimundi.core.menu import Menu
# Graphics engine = Objects
from oculimundi.graphics_engine.renderer import Renderer
from oculimundi.graphics_engine.object3D.scene import Scene, Group
from oculimundi.graphics_engine.object3D.camera import Camera
from oculimundi.graphics_engine.object3D.mesh import Mesh
from oculimundi.graphics_engine.object3D.movement_rig import MovementRig
# Graphics engine = Geometries
from oculimundi.graphics_engine.geometry.parametric_geometry import SphereGeometry, CylinderGeometry
from oculimundi.graphics_engine.geometry.rectangle_geometry import RectangleGeometry
# Graphics engine = Materials
from oculimundi.graphics_engine.texture import Texture
from oculimundi.graphics_engine.text_texture import TextTexture
from oculimundi.graphics_engine.materials.basic_material import PointMaterial
from oculimundi.graphics_engine.materials.surface_material import SurfaceMaterial
from oculimundi.graphics_engine.materials.texture_material import TextureMaterial
from oculimundi.graphics_engine.materials.phong_material import PhongMaterial
# Graphics engine = Light
from oculimundi.graphics_engine.light.light import AmbientLight, DirectionalLight, PointLight

class GameModes(Enum):
    MENU = 1
    PLAY = 2
    GAMEOVER = 3

class Game:

    def __init__(self, screen_size=[800,600]):
        
        # Initialize pygame
        pg.init()
        display_flags = pg.DOUBLEBUF | pg.OPENGL
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLEBUFFERS, 1)
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLESAMPLES, 4)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        self.screen = pg.display.set_mode(screen_size, display_flags)
        pg.display.set_caption("Oculi Mundi")
        
        # Game settings
        self.state = GameModes.MENU
        self.running = True
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.input = Input()

    def startup(self):

        # General
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera( aspect_ratio=800/600)
        self.hud_camera = Camera()
        self.hud_camera.set_ortographic(0, 800, 0, 600, 1, -1)
        self.rig = MovementRig()
        self.rig.add( self.camera )
        self.rig.set_position([0,5,40])
        self.scene.add(self.rig)

        # Sky
        skyGeometry = SphereGeometry(80)
        skyMaterial = PointMaterial(properties={ "base_color": [0.65, 0.68, 0.78]})
        self.sky = Mesh( skyGeometry, skyMaterial )
        self.sky.set_position([0, 0, 0])
        self.scene.add(self.sky)

        # TITLE
        title_geo = RectangleGeometry(
            width=400,
            height=125,
            position=[600, 400],
            alignment=[1,0]
        )
        title = TextureMaterial( TextTexture(
            text= "OCULI  MUNDI",
            font_size= 40,
            font_color=[180, 190, 254],
            transparent= True
        ))
        title_mesh = Mesh(title_geo, title)

        # GAME OVER
        gover = TextureMaterial( TextTexture(
            text= "GAME  OVER",
            font_size= 40,
            font_color=[180, 190, 254],
            transparent= True
        ))
        gover_mesh = Mesh(title_geo, gover)

        # START
        start_geo = RectangleGeometry(
            width=120,
            height=80,
            position=[470, 260],
            alignment=[1,0]
        )
        start = TextureMaterial( TextTexture(
            text= "START",
            font_size= 28,
            font_color=[205, 214, 244],
            transparent= True
        ))
        start_mesh = Mesh(start_geo, start)

        # RESTART
        restart = TextureMaterial( TextTexture(
            text= "RESTART",
            font_size= 28,
            font_color=[205, 214, 244],
            transparent= True
        ))
        restart_mesh = Mesh(start_geo, restart)

        # QUIT
        quit_geo = RectangleGeometry(
            width=120,
            height=70,
            position=[470, 190],
            alignment=[1,0]
        )
        quit = TextureMaterial( TextTexture(
            text= "QUIT",
            font_size= 28,
            font_color=[205, 214, 244],
            transparent= True
        ))
        quit_mesh = Mesh(quit_geo, quit)

        # FOCUS
        focus_geo = RectangleGeometry(
            width=180,
            height=100,
            position=[500, 260],
            alignment=[1,0]
        )
        focus = TextureMaterial( TextTexture(
            text= "<                          >",
            font_size= 28,
            font_color=[235, 160, 172],
            transparent= True
        ))
        focus_mesh = Mesh(focus_geo, focus)

        # Menu and menu scene
        self.menu = Menu()
        self.menu_scene = Scene()
        self.menu_scene.add(title_mesh)
        self.menu_scene.add(start_mesh)
        self.menu_scene.add(quit_mesh)
        self.menu_scene.add(focus_mesh)

        # Game over and game over scene
        self.gover_scene = Scene()
        self.gover_scene.add(gover_mesh)
        self.gover_scene.add(restart_mesh)
        self.gover_scene.add(quit_mesh)
        self.gover_scene.add(focus_mesh)

        # Spaceship
        material = PhongMaterial(properties={ "base_color": [0.58, 0.89, 0.84]})
        shipbase = Mesh(CylinderGeometry(1, 5), material)
        wings = Mesh(RectangleGeometry(9, 2), material)
        self.spaceship = Group()
        self.spaceship.add(shipbase)
        self.spaceship.add(wings)
        self.spaceship.rotateX(3.14 / 2)
        self.spaceship.set_position([0,0,0])

        # Eye
        text_mat = Texture("oculimundi/graphics_engine/textures/eye.png")
        boss_mat = PhongMaterial(texture=text_mat, properties={ "base_color": [0.98, 0.7, 0.53]})
        self.boss = Mesh(SphereGeometry(10), boss_mat)
        self.boss.set_position([0,5,-30])
        self.boss.rotateX(3.14)

        # Bullets
        self.bullets = Group()

        # Level and level scene
        self.level = Level()
        self.level_scene = Scene()
        self.level_scene.add(self.spaceship)
        self.level_scene.add(self.boss)
        self.level_scene.add(self.bullets)

        # Light
        ambient_light = AmbientLight(color=[0.4, 0.4, 0.4])
        self.level_scene.add(ambient_light)
        directional_light = DirectionalLight(color=[0.8,0.8,0.8], direction=[-60,-60,0])
        self.level_scene.add(directional_light)
        point_light = PointLight(color=[0.6,0.3,0], position=[60, 30, 10])
        self.scene.add(point_light)

    def update(self):
        # Update background
        self.sky.rotateY(0.01)
        self.sky.rotateX(0.02)
        if self.state == GameModes.PLAY:
            # Check if someone is dead
            if self.level.spaceship.health < 0:
                self.state = GameModes.GAMEOVER
                return
            if self.level.boss.health < 0:
                self.state = GameModes.MENU
                return
            self.update_play()
        elif self.state == GameModes.MENU:
            self.update_menu()
        elif self.state == GameModes.GAMEOVER:
            self.update_menu()
        self.rig.update(self.input, self.delta_time)
    
    def draw(self):
        self.renderer.render(self.scene, self.camera)
        if self.state == GameModes.PLAY:
            self.renderer.render(scene=self.level_scene, camera=self.camera, clear_color=False)
        elif self.state == GameModes.MENU:
            self.renderer.render(scene=self.menu_scene, camera=self.hud_camera, clear_color=False)
        elif self.state == GameModes.GAMEOVER:
            self.renderer.render(scene=self.gover_scene, camera=self.hud_camera, clear_color=False)
    
    def update_play(self):

        # Update level
        self.level.update(self.input, self.delta_time)
        self.spaceship.set_position(self.level.spaceship.position)

        # Update bullets (and another trashy code)
        for bullet in self.level.bullets:
            if bullet.mesh == None:
                bullet.mesh = self.create_bullet_mesh(bullet)
                bullet.mesh.set_position(bullet.position)
                self.bullets.add(bullet.mesh)
            else:
                if bullet.has_hit:
                    self.bullets.remove(bullet.mesh)
                bullet.mesh.set_position(bullet.position)
        
        # Delete bullets from level.bullets list
        self.level.bullets = [ bullet for bullet in self.level.bullets if bullet.has_hit == False ]

    def create_bullet_mesh(self, bullet):

        if bullet.type == BulletTypes.RAY:
            material = PhongMaterial(properties={ "base_color": [0.796, 0.65, 0.97]})
        if bullet.type == BulletTypes.FLOWER:
            material = PhongMaterial(properties={ "base_color": [0.96, 0.88, 0.86]})
        if bullet.type == BulletTypes.RINGS:
            material = PhongMaterial(properties={ "base_color": [0.95, 0.8, 0.8]})
        if bullet.type == BulletTypes.PLAYER:
            material = PhongMaterial(properties={ "base_color": [0.796, 0.76, 0.91]})
        
        return Mesh( SphereGeometry(0.7),material)

    def update_menu(self):
        self.menu.update(self.input)
        if self.menu.focus == 1:
            self.menu_scene.children[3].set_position([0, 5, 0])
        if self.menu.focus == 0:
            self.menu_scene.children[3].set_position([0, -75, 0])
        if self.menu.choice == 1:
            self.state = GameModes.PLAY
            self.bullets.children.clear()
            self.level.clean()
            self.menu.choice = -1
        if self.menu.choice == 0:
            self.running = False
            self.menu.choice = -1

    def run(self):
        self.startup()
        while self.running:
            self.input.update()
            self.update()
            self.draw()
            if self.input.quit:
                self.running = False
            pg.display.flip()
            self.clock.tick(60)
            self.delta_time = self.clock.get_time() / 1000
        pg.quit()
        sys.exit()
