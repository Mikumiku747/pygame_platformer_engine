#-------------------------------------------------------------------------------
# Name:        main
# Purpose:     Contains the main game loop, game logic, that kinda thing. May be
#              changed later to only include the main game loop and central
#              logic if possible.
#
# Author:      Daniel Selmes
# Version:     1.0
# Created:     24/06/2014
#-------------------------------------------------------------------------------

#Imports
import vector
import physics
import collision

def main():
    box1 = physics.Rectangular_dynamic(mass=2, displacement=vector.Vector2(5.0, 0), proportion=vector.Vector2(10.0, 10.0))
    box2 = physics.Rectangular_dynamic(mass=2, displacement=vector.Vector2(25.0, 0), proportion=vector.Vector2(10.0, 10.0))
    print(collision.collide(box1, box2))
    box1.apply_force(vector.Vector2(4.0, 0.0))
    box2.apply_force(vector.Vector2(1.0, 0.0))
    while not collision.collide(box1.next(), box2.next()):
        box1.update()
        box2.update()
##        print("box1 position: {}\nbox2 position: {}".format(box1.displacement, box2.displacement))
    print("Box1 and Box2 are about to collide!")
    print("box1: {}\nbox2: {}".format(box1, box2))
    print("They are colliding!")
    print("box1: {}\nbox2: {}".format(box1.next(), box2.next()))

if __name__ == '__main__':
    main()
