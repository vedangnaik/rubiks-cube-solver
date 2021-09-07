from Solvers.Solver import Solver
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
        # a.draw()

        for _ in range(random.randint(10, 65)):
            a.turn(random.choice([F, F_, F2, R, R_, R2, B, B_, B2, L, L_, L2, U, U_, U2, D, D_, D2]))
        # a.draw()

        s = CFOPSolver(a)
        s.solve()
        # a.draw()

        solvedCube = [
            [
                ['r', 'r', 'r'],
                ['r', 'r', 'r'],
                ['r', 'r', 'r'],
            ],
            [
                ['g', 'g', 'g'],
                ['g', 'g', 'g'],
                ['g', 'g', 'g'],
            ],
            [
                ['o', 'o', 'o'],
                ['o', 'o', 'o'],
                ['o', 'o', 'o'],
            ],
            [
                ['b', 'b', 'b'],
                ['b', 'b', 'b'],
                ['b', 'b', 'b'],
            ],
            [
                ['y', 'y', 'y'],
                ['y', 'y', 'y'],
                ['y', 'y', 'y'],
            ],
            [
                ['w', 'w', 'w'],
                ['w', 'w', 'w'],
                ['w', 'w', 'w'],
            ],
        ]

        solved = True
        for face in range(6):
            for row in range(3):
                for col in range(3):
                    if solvedCube[face][row][col] != a.cubeRepr[face][row][col]:
                        solved = False
        assert(solved)