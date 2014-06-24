#-------------------------------------------------------------------------------
# Name:        physics
# Purpose:     Some assorted physics stuff needed from the project
#
# Author:      Daniel Selmes
#
# Created:     24/06/2014
#-------------------------------------------------------------------------------

class VectorMathError(Exception):
    pass

class Vector(list):
    """A list with some extra methods.
    A list with some extra methods for clarification/simplicity as well as
    overrides to make it behave more like a vector. May specialize this into
    other types that realte to physics properties such as velocity or
    displacement. """

    def v_add(self, other):
        """Adds this to other as if the two were vecotrs.
         Adds this to other as if the two were vecotrs. Any components missing
         from the second vector are simply set to 0. (No effect.)"""
        for component in self:
            i = self.index(component)
            if len(other) >= i+1:
                self[self.index(component)]+=other[i]
            return self

    def x_component(self):
        "Get the x component of this vector."
        return(self[0])
    def y_component(self):
        "Get the y component of this vector."
        return(self[1])
    #unused because I don't know how the z component works yet...
##    def z_component(self):
##        "Get the z component of this vector."
##        return(self[2])

def main():
    d1 = Vector([10, 10])
    d2 = Vector([0, -10])
    print("d1 = {}\nd2 = {}".format(d1, d2))
    d3 = d1.v_add(d2)
    print(d3)

if __name__ == "__main__":
    main()
