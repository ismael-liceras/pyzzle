#/usr/bin/env python

#Import Modules
#import pygame
from gameengine import GameEngine
from sys import argv


def main():

    if len(argv) > 1:
        image = argv[1]

    ge = GameEngine(image)

    while 1:
        if ge.handle_events() == -1:
            return

if __name__ == '__main__': main()
