#-------------------------------------------------------------------------------
# Name:        Vectors
# Purpose:     For vectors and basic vector math
#
# Author:      Daniel
#
# Created:     05/09/2014
# Copyright:   (c) Daniel 2014
# Version:     1.0
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#required modules
import math
from math import sqrt, pow

def inv_tan(ratio):
    "Gives the inverse tan of ratio in degrees."
    return math.degrees(math.atan(ratio))

def inv_sin(ratio):
    "Gives the inverse sin of ratio in degrees."
    return math.degrees(math.asin(ratio))

def inv_cos(ratio):
    "Gives the inverse cos of ratio in degrees."
    return math.degrees(math.acos(ratio))

class Vector2:
    """2 dimensional vector.
    Be sure to subclass this class when making your own so that the methods
    work. Also, be careful that you try to feed the vectors floating point
    numbers so that measurements remain accurate.
    Also note that most functions will only take literal numbers when asking for
    a scalar value. """

    def __init__(self, x=0.0, y=0.0):
        "A two dimensional vector with components X and Y."
        self.x = x
        self.y = y

    def contruct_two_part(self, magnitude=0.0, direction=0.0):
        """Redefine the vector using a magnitude and rotation.
        Magnitude is virtual "length" of the vector.
        Direction is rotation, in degrees, between the positive x and positive y
        axis. For pygame, this is along the horizontal axis moving clockwise
        towards the vertical axis. """
        assert isinstance(magnitude, (int, float, long)), "You need to supply a scalar number as a magnitude."
        assert isinstance(direction, (int, float, long)), "You need to supply a scalar number in degrees as a direction. "

        #Obtain the X component
        self.x = magnitude*math.degrees(math.cos(direction))
        #Obtain the Y component
        self.y = magnitude*math.degrees(math.sin(direction))

    def magnitude(self):
        "Gives the magnitude of the vector."
        return sqrt(pow(self.x, 2) + pow(self.y, 2))
        #Use distance formula to obtain the magnitude.

    def direction(self):
        "Gives the angle between the X axis and the vector."
        return inv_tan(self.y/self.x)

    def sum(self, other):
        "Adds this vector to another 2D vector."
        assert isinstance(other, Vector2), "You can only add 2D vectors with other 2D vectors."
        return Vector2(self.x+other.x, self.y+other.y)

    def diff(self, other):
        "Subtracts this vector from another vector."
        assert isinstance(other, Vector2), "You can only subtract 2D vectors with other 2D vectors."
        return Vector2(self.x-other.x, self.y-other.y)

    def multiply(self, scalar):
        "Multiplies this vector by a scalar value."
        assert isinstance(scalar, (int, long, float)), "You can only multiply vectors by scalars with this method."
        return Vector2(self.x*scalar, self.y*scalar)

    def scalar_product(self, other):
        "Scalar product of this vector and another vector."
        assert isinstance(other, Vector2), "You must use 2 2D vectors when finding the scalar product."
        return self.x*other.x + self.y*other.y + self.z*other.z

##    def vector_product(self, other):
##        "Gives the vector product of this and another vector. "
##        assert()

    def __str__(self):
        return "2D Vector: x={x}, y={y}".format(x=self.x, y=self.y)
    def __repr__(self):
        return "Vector2({x},{y})".format(x=self.x, y=self.y)

def main():
    v1 = Vector2(5.0, 5.0)
    v2 = Vector2(3.0, 4.0)

    #Check direction and magnitude are working
    assert (v1.direction()==45.0)
    assert (v1.magnitude()==sqrt(50))
    assert (v2.direction()==inv_tan(4.0/3.0))
    assert (v2.magnitude()==5.0)

    #Check addition and subtraction are working
    assert (v1.sum(v2).x == 8.0)
    assert (v1.diff(v2).y == 1.0)

    #If all that works, the module should be working!

    print("Vector module works! Yay!")

if __name__ == '__main__':
    main()
