#-------------------------------------------------------------------------------
# Name:        physics
# Purpose:     General classes to represent the physical properties of an object
#              in space.
#
# Author:      Daniel
#
# Created:     05/09/2014
# Copyright:   (c) Daniel 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import vector

class Rectangular:
    def __init__(self, displacement=vector.Vector2(0.0, 0.0),
                        proportion=vector.Vector2(1.0, 1.0),
                        velocity=vector.Vector2(0.0, 0.0),
                        acceleration=vector.Vector2(0.0, 0.0),
                        mass=1.0):
        "A rectangular physical object."

def main():
    pass

if __name__ == '__main__':
    main()
