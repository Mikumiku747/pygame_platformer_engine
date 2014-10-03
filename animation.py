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

class animation:
	"A grouped list of images with some fancy stuff."
	def init(self, images, initial=0):
		"Create an animation from a list of surfaces"
		self.images=images
		self.frame=initial
		if self.frame >= len(self.images):
				self.frame=0
		
	def current(self):
		"Return the current image of the animation."
		return self.images[self.frame]
		
	def animate(self, time=1):
		"Advances the animation by a number of frames."
		for i in range(time):
			self.frame += 1
			if self.frame >= len(self.images):
				self.frame=0
			

def load_image_set(folder_path, prefix='', ext=".png"):
    "Loads a bunch of images from a folder, returns a list of surfaces."
    ret = []
    for file in os.listdir(folder_path):
		if file.startswith(prefix) and file.endswith(ext):
			ret.append(load("{}/{}".format(folder_path, file)))
	return ret
		


def main():
    pass

if __name__ == '__main__':
    main()
