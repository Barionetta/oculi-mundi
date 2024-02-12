# -*- coding: utf-8 -*-
"""
    This is the main file of the project
"""
__version__ = '0.1.0'
__author__ = 'Katarzyna Matuszek'

from src.game import Game

def main():
    print("Oculi Mundi Shooter")
    game = Game(screen_size=[800,600])
    game.run()
    
if __name__ == "__main__":
    main()
