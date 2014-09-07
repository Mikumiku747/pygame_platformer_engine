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
                        default_accel=vector.Vector2(0.0, 0.0),
                        mass=1.0, dampening=1.0):
        self.displacement = displacement #Centre of body
        self.velocity = velocity #In PX.FR^-1
        self.acceleration = vector.Vector2() #In PX.FR^-2
        self.mass = float(mass) #In MU
        self.default_accel = default_accel #Accel. reset value
        self.dampening = float(dampening) #Amount of arbitrary drag.

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

class Rectangular_dynamic(dynamic_body):
    """A rectangular physical object, which has classical interactions with the environment."""
    def __init__(self, displacement=vector.Vector2(0.0, 0.0),
                        proportion=vector.Vector2(1.0,1.0),
                        velocity=vector.Vector2(0.0, 0.0),
                        default_accel=vector.Vector2(0.0, 0.0),
                        mass=1.0, dampening=1.0):
        dynamic_body.__init__(self, displacement=displacement, velocity=velocity, default_accel=default_accel, mass=mass, dampening=dampening)
        #Initialise the physical object
        self.proportion = proportion #Give the rectangular a proportion

    def __str__(self):
        return "Rectangular dynamic object: Mass={mass}, Displacement={disp}, Velocity={vel}".format(mass=self.mass, disp=repr(self.displacement), vel=repr(self.velocity))
    def __repr__(self):
        return "Rectangular_dynamic(\ndisplacement={disp},\nproportion={size},\nvelocity={vel},\ndefault_accel={default_accel},\nacceleration={accel},\nmass={mass}".format(disp=repr(self.displacement), size=repr(self.proportion), vel=repr(self.velocity), default_accel=repr(self.default_accel), accel=repr(self.acceleration), mass=self.mass)


def main():
    pass

if __name__ == '__main__':
    main()
