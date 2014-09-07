#-------------------------------------------------------------------------------
# Name:        collision
# Purpose:     Allows testing of intersection between various shapes
#
# Author:      Daniel
#
# Created:     07/09/2014
# Version:     1.0
# Copyright:   (c) Daniel 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from pygame.rect import Rect as Rect
import physics

class CollisionException(Exception):
    pass

def rectangle_rectangle(x1, y1, w1, h1, x2, y2, w2, h2):
    "Test for intersection of rectangles 1 and 2, centres x,y, dimensions w,h"
    a = Rect((x1-w1/2, y1-h1/2, w1, h1))
    b = Rect((x2-w2/2, y2-h2/2, w2, h2))
    return bool(a.colliderect(b))

def collide(body1, body2):
    if (isinstance(body1, physics.Rectangular_dynamic) and isinstance(body2, physics.Rectangular_dynamic)):
        #Test for collision between 2 rectangles
        return rectangle_rectangle(body1.displacement.x, body1.displacement.y, body1.proportion.x, body1.proportion.y, body2.displacement.x, body2.displacement.y, body2.proportion.x, body2.proportion.y)
    else:
        raise CollisionException("There is no suitable collision algorithm for these two types of bodies:", body1, body2)

def main():
    pass

if __name__ == '__main__':
    main()
