# -*- coding: utf-8 -*-
"""
    This is the main file of the project
"""

from oculimundi.game import Game

def main():
    print("Oculi Mundi Shooter")
    game = Game(screen_size=[800,600])
    game.run()