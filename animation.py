#-------------------------------------------------------------------------------
# Name:        animation
# Purpose:     To provide a library to easily animate a sprite. Also serves to
#               easily load in images and group them.
#
# Author:      Daniel
#
# Created:     17/09/2014
# Version:     1.0
# Copyright:   (c) Daniel 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Imports
import pygame
pygame.init()

from os import
load = pygame.image.load

def load_spite_set(folder_path, prefix='', ext=".png"):
    "Loads a bunch of images from a folder, returns a list of surfaces."
    ret = []
    for file in os.listdir(folder_path):
		if file.startswith(prefix) and file.endswith(ext):
			ret.append(load("{}/{}".format(folder_path, file)))
		


def main():
    pass

if __name__ == '__main__':
    main()
