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
import copy
import collision

#Module Notes
#------------
#The physics module allows you to simulate physics between objects that exist in
#a virtual space. Note that you must manually test for collision between objects
#that exist in the game. The module recommends the following standard units:
#   Distance: Pixels (PX)
#   Mass: Mass Units (MU)
#   Time: Frame (FR)
#The module reccomends the following derived units
#   Velocity: Pixels per frame (PX.FR^-1)
#   Force: DigiNewtons (DN) (MU.PX.FR^-2)
#   Acceleration: Pixels per frame squared (PX.FR^-2)
#
# General tips:
# Acceleration - Acceleration must be constantly applied on an object before
#               every update. This is because acceleration is neutralised every
#               single frame. If you want to apply a constant acceleration, add
#               it to the default force attribute.
#
# Corners - Corners of an object are given as a tuple of vectors, in the
#           following order, and their appearance in pygame:
#           - X least, Y least (Top left)
#           - X most,  Y least (Top Right)
#           - X least, Y most  (Bottom Left)
#           - X most,  Y most  (Bottom Right)

class Dynamic_body:
    "A generic physical body with classical reactions to it's environment."
    def __init__(self, displacement=vector.Vector2(0.0, 0.0),
                        velocity=vector.Vector2(0.0, 0.0),
                        acceleration=vector.Vector2(0.0, 0.0),
                        default_accel=vector.Vector2(0.0, 0.0),
                        mass=1.0, dampening=1.0, colliders = []):
        self.displacement = displacement #Centre of body
        self.velocity = velocity #In PX.FR^-1
        self.acceleration = vector.Vector2() #In PX.FR^-2
        self.mass = float(mass) #In MU
        self.default_accel = default_accel #Accel. reset value
        self.dampening = float(dampening) #Amount of arbitrary drag.
        self.colliders = colliders

    def apply_force(self, force=vector.Vector2()):
        """Apply a force (in PX.FR^-2) to this object.
        Returns the change in acceleration."""
        self.acceleration=self.acceleration.sum(force.divide(self.mass))
        return force.divide(self.mass)

    def dampen(self, multiplier):
        "Dampen this object by apply the multiplier to it's velocity. Returns the change in velocity."
        assert isinstance(multiplier, (int, long, float)), "The dampen multiplier must be a number."
        original = self.velocity
        self.velocity = self.velocity.multiply(multiplier)
        return original.diff(self.velocity)

    def update(self):
        "Update the physical state of this object by one frame."
        self.velocity = self.velocity.sum(self.acceleration) #Apply the acceleration to the object's velocity
        self.displacement = self.displacement.sum(self.velocity) #Apply the object's velocity to it's displacement
        self.velocity = self.velocity.multiply(self.dampening) #Dampen the velocity of the object
        self.acceleration = self.default_accel #Reset the acceleration of the object

    def next(self, time=1):
        "Returns an exact copy of this object time updates in the future."
        future = copy.deepcopy(self)
        for iteration in range(time):
            future.update()
        return future

    def repr(self):
        return "Dynamic body(displacement={}, velocity={}, acceleration = {}, default_accel={}, mass={}, dampening={}, colliders = {})".format(
    self.displacement, self.velocity, self.acceleration, self.default_accel, self.mass, self.dampening, self.colliders)

    def collide(self, other):
        if collision.check_intersect(self, other):
            u1x, u1y, u2x, u2y = self.velocity.x, self.velocity.y, other.velocity.x, other.velocity.y
            m1, m2 = self.mass, other.mass
            #Find new velocity of each object
            v1x = (u1x*(m1-m2)+2*m2*u2x)/(m1+m2)
            v1y = (u1y*(m1-m2)+2*m2*u2x)/(m1+m2)
            v2x = (u2x*(m2-m1)+2*m1*u1x)/(m1+m2)
            v2y = (u2y*(m2-m1)+2*m1*u1y)/(m1+m2)
            #Apply these new velocities to the objects
            self.velocity.x, self.velocity.y = v1x, v1y
            other.velocity.x, other.velocity.y = v2x, v2y

def main():
    pass

if __name__ == '__main__':
    main()
