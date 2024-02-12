# -*- coding: utf-8 -*-
"""
    This is the file of Renderer class
    Based on "Developing Graphics Frameworks with Python and OpenGL"
"""

from OpenGL.GL import *
from src.graphics_engine.object3D.mesh import Mesh
from src.graphics_engine.light.light import Light

class Renderer(object):
    def __init__(self, clear_color=[0.067, 0.067, 0.106]):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_MULTISAMPLE)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glClearColor(clear_color[0], clear_color[1], clear_color[2], 1)

    def render(self, scene, camera, clear_color=True, clear_depth=True):

        if clear_color:
            glClear(GL_COLOR_BUFFER_BIT)
        if clear_depth:
            glClear(GL_DEPTH_BUFFER_BIT)

        camera.update_view_matrix()
        
        descendant_list = scene.get_descendant_list()
        mesh_filter = lambda x: isinstance(x, Mesh)
        mesh_list = list(filter(mesh_filter, descendant_list))

        light_filter = lambda x: isinstance(x, Light)
        light_list = list(filter(light_filter, descendant_list))
        while len(light_list) < 4:
            light_list.append( Light() )

        for mesh in mesh_list:
            if not mesh.is_visible:
                continue
            glUseProgram( mesh.material.program_ref)
            glBindVertexArray( mesh.VAO)
            mesh.material.uniforms["model_matrix"].data = mesh.get_world_matrix()
            mesh.material.uniforms["view_matrix"].data = camera.view_matrix
            mesh.material.uniforms["projection_matrix"].data = camera.projection_matrix

            if "light0" in mesh.material.uniforms.keys():
                for light_number in range(4):
                    light_name = "light" + str(light_number)
                    light_object = light_list[light_number]
                    mesh.material.uniforms[light_name].data = light_object
            
            if "view_position" in mesh.material.uniforms.keys():
                mesh.material.uniforms["view_position"].data = camera.get_world_position()

            for variable_name, uniform_object in mesh.material.uniforms.items():
                uniform_object.upload_data()
            mesh.material.update_render_settings()
            glDrawArrays( mesh.material.settings["draw_style"], 0, mesh.geometry.vertex_count)
