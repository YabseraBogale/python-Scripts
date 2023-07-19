"""
In geometry, a cube is a three-dimensional solid object bounded by six square faces, facets or sides, with three meeting at each vertex.The cube is the only regular hexahedron and is one of the five Platonic solids. It has 12 edges, 6 faces and 8 vertices.The cube is also a square parallelepiped, an equilateral cuboid and a right rhombohedron. It is a regular square prism in three orientations, and a trigonal trapezohedron in four orientations.

You are given a task of finding a if the provided value is a perfect cube!


"""

import numpy as np
def you_are_a_cube(cube):
    #your code here
    ans=int(np.cbrt(cube))
    return ans*ans*ans==cube

print(you_are_a_cube(27))
