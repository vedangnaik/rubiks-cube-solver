from Cube.Cube import Cube
from Cube.Move import *
from colorama import init
from Solvers.CFOPSolver import CFOPSolver

if __name__ == "__main__":
    import random
    init(autoreset=True)

    for test in range(5000):
        print(test)
        a = Cube()

        for _ in range(random.randint(10, 65)):
            a.turn(random.choice([F, F_, F2, R, R_, R2, B, B_, B2, L, L_, L2, U, U_, U2, D, D_, D2]))

        s = CFOPSolver(a)
        s.solve()

        assert(a.cubeRepr[Cube.FRONT][2][1] == 'r' and a.cubeRepr[Cube.DOWN][0][1] == 'w')
        assert(a.cubeRepr[Cube.RIGHT][2][1] == 'g' and a.cubeRepr[Cube.DOWN][1][2] == 'w')
        assert(a.cubeRepr[Cube.BACK][2][1] == 'o' and a.cubeRepr[Cube.DOWN][2][1] == 'w')
        assert(a.cubeRepr[Cube.LEFT][2][1] == 'b' and a.cubeRepr[Cube.DOWN][1][0] == 'w')

        assert(a.cubeRepr[Cube.FRONT][2][2] == 'r' and a.cubeRepr[Cube.RIGHT][2][0] == 'g' and a.cubeRepr[Cube.DOWN][0][2] == 'w')
        assert(a.cubeRepr[Cube.RIGHT][2][2] == 'g' and a.cubeRepr[Cube.BACK][2][0] == 'o' and a.cubeRepr[Cube.DOWN][2][2] == 'w')
        assert(a.cubeRepr[Cube.BACK][2][2] == 'o' and a.cubeRepr[Cube.LEFT][2][0] == 'b' and a.cubeRepr[Cube.DOWN][2][0] == 'w')
        assert(a.cubeRepr[Cube.LEFT][2][2] == 'b' and a.cubeRepr[Cube.FRONT][2][0] == 'r' and a.cubeRepr[Cube.DOWN][0][0] == 'w')

        assert(a.cubeRepr[Cube.FRONT][1][2] == 'r' and a.cubeRepr[Cube.RIGHT][1][0] == 'g')
        assert(a.cubeRepr[Cube.RIGHT][1][2] == 'g' and a.cubeRepr[Cube.BACK][1][0] == 'o')
        assert(a.cubeRepr[Cube.BACK][1][2] == 'o' and a.cubeRepr[Cube.LEFT][1][0] == 'b')
        assert(a.cubeRepr[Cube.LEFT][1][2] == 'b' and a.cubeRepr[Cube.FRONT][1][0] == 'r')