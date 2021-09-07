from Cube.Cube import Cube
from Cube.Move import *
from colorama import init
from Solvers.CFOPSolver import CFOPSolver

if __name__ == "__main__":
    import random
    init(autoreset=True)

    # a = Cube()
    # a.draw()
    # exit(0)

    for test in range(1000):
        print(test)
        a = Cube()
        # a.draw()

        for _ in range(random.randint(10, 65)):
            a.turn(random.choice([F, F_, F2, R, R_, R2, B, B_, B2, L, L_, L2, U, U_, U2, D, D_, D2]))
        # a.draw()

        s = CFOPSolver(a)
        s.solve()
        # a.draw()

        assert(a.cubeRepr[Cube.FRONT][2][2] == 'r' and a.cubeRepr[Cube.RIGHT][2][0] == 'g' and a.cubeRepr[Cube.DOWN][0][2] == 'w')
        # assert(a.cubeRepr[Cube.RIGHT][2][1] == 'g' and a.cubeRepr[Cube.DOWN][0][1] == 'w')
        # assert(a.cubeRepr[Cube.BACK][2][1] == 'o' and a.cubeRepr[Cube.DOWN][0][1] == 'w')
        # assert(a.cubeRepr[Cube.LEFT][2][1] == 'b' and a.cubeRepr[Cube.DOWN][0][1] == 'w')