#/usr/bin/env python

#Import Modules
#import pygame
from gameengine import GameEngine
from sys import argv


def main():

    image = None
    n = None
    if len(argv) == 3:
        for i in range(1, 3):
            if argv[i][:4] == '--n=':
                n = argv[i][4:]
            else:
                image = argv[i]

    if (image is None) or (n is None):
        print "usage: pyzzle --n=<number> image_file"
        exit()

    print argv

    exit()
    ge = GameEngine(image, n)

    while 1:
        if ge.handle_events() == -1:
            return

if __name__ == '__main__': main()
