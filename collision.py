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
from pygame.rect import Rect
import physics
import vector

def rectangle_rectangle(x1, y1, w1, h1, x2, y2, w2, h2):
    "Test for intersection of rectangles 1 and 2, centres x,y, dimensions w,h"
    a = Rect((x1-w1/2, y1-h1/2, w1, h1))
    b = Rect((x2-w2/2, y2-h2/2, w2, h2))
    return bool(a.colliderect(b))

class rectangle_collider():
    "Rectangle shaped collider object"
    def __init__(self, proportion=vector.Vector2(1.0, 1.0), offset=vector.Vector2()):
        self.proportion = proportion
        self.offset = offset

def check_intersect(body1, body2):
    "Checks if any part of two bodies are intersecting."
    for collider1 in body1.colliders:
        for collider2 in body2.colliders:
            if (isinstance(collider1, rectangle_collider) and
                isinstance(collider2, rectangle_collider)):
                    if rectangle_rectangle(body1.displacement.x+collider1.offset.x,
                                           body1.displacement.y+collider1.offset.x,
                                           collider1.proportion.x,
                                           collider1.proportion.y,
                                           body2.displacement.x+collider2.offset.x,
                                           body2.displacement.y+collider2.offset.x,
                                           collider2.proportion.x,
                                           collider2.proportion.y): return True
                    else:
                        raise Exception("Could not test collision, an alogrithm does not exist yet for testing between these two colliders:", collider1, collider2)
                    return False


def main():
    pass

if __name__ == '__main__':
    main()
