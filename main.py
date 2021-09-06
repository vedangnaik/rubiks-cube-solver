from Cube.Cube import Cube
from colorama import init
from Solvers.CFOPSolver import CFOPSolver

if __name__ == "__main__":
    import random
    init(autoreset=True)

    for test in range(1):
        print(test)
        a = Cube()
        a.draw()

        for _ in range(random.randint(10, 65)):
            a.turn(random.choice(list(Cube.Move)[:18]))
        a.draw()

        s = CFOPSolver(a)
        s.solve()
        a.draw()        

        assert(a.cubeRepr[Cube.FRONT][2][1] == 'r' and a.cubeRepr[Cube.DOWN][0][1] == 'w')
        assert(a.cubeRepr[Cube.RIGHT][2][1] == 'g' and a.cubeRepr[Cube.DOWN][0][1] == 'w')
        assert(a.cubeRepr[Cube.BACK][2][1] == 'o' and a.cubeRepr[Cube.DOWN][0][1] == 'w')
        assert(a.cubeRepr[Cube.LEFT][2][1] == 'b' and a.cubeRepr[Cube.DOWN][0][1] == 'w')