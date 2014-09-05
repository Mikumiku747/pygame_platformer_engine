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

#Required modules
import vector

#Module Notes
#------------
#The physics module allows you to simulate physics between objects that exist in
#a virtual space. Note that you must manually test for collision between objects
#that exist in the game. The module recommends the following standard units:
#   Distance: Pixels (PX)
#   Mass: Mass Units (MU) or grams (g)
#   Time: Frame (FR)
#
#Application:
# Acceleration - Acceleration must be constantly applied on an object before
#               every update. This is because acceleration is neutralised every
#               single frame. If you want to apply a constant acceleration, add
#               it to the default force attribute.
#
# Corners - Corners of an object are given as a tuple of vectors


class Rectangular_dynamic:
    """A rectangular physical object, which has classical interactions with the environment."""
    def __init__(self, displacement=vector.Vector2(0.0, 0.0),
                        proportion=vector.Vector2(1.0, 1.0),
                        velocity=vector.Vector2(0.0, 0.0),
                        acceleration=vector.Vector2(0.0, 0.0),
                        mass=1.0):
        "A rectangular physical object."
        self.displacement = displacement #Centre of body
        self.proportion = proportion #Size of body
        self.velocity = velocity
        self.acceleration = acceleration
        self.mass = mass #In MU
        self.default_force = vector.Vector2(0.0, 0.0) #Accel. reset value

    def corners(self):
        "Get the corners of this rectangle as displacement vectors."
        return (vector.Vector2(self.displacement.x-(self.proportion.x/2),
                               self.displacement.y-(self.proportion.y/2)),
                vector.Vector2(self.displacement.x+(self.proportion.x/2),
                               self.displacement.y-(self.proportion.y/2)),
                vector.Vector2(self.displacement.x-(self.proportion.x/2),
                               self.displacement.y+(self.proportion.y/2)),
                vector.Vector2(self.displacement.x+(self.proportion.x/2),
                               self.displacement.y+(self.proportion.y/2)))


def main():
    pass

if __name__ == '__main__':
    main()
