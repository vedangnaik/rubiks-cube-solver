from Solvers.Solver import Solver
from Cube.Cube import Cube

class CFOPSolver(Solver):
    __whiteCrossMoves = [
        # Bottom layer edges.
        ((Cube.FRONT, 2, 1), (Cube.DOWN, 0, 1), []),
        ((Cube.DOWN, 0, 1), (Cube.FRONT, 2, 1), [Cube.Move.F_, Cube.Move.D, Cube.Move.R_, Cube.Move.D_]),
        ((Cube.RIGHT, 2, 1), (Cube.DOWN, 1, 2), [Cube.Move.R2, Cube.Move.U, Cube.Move.F2]),
        ((Cube.DOWN, 1, 2), (Cube.RIGHT, 2, 1), [Cube.Move.R, Cube.Move.F]),
        ((Cube.BACK, 2, 1), (Cube.DOWN, 2, 1), [Cube.Move.B2, Cube.Move.U2, Cube.Move.F2]),
        ((Cube.DOWN, 2, 1), (Cube.BACK, 2, 1), [Cube.Move.B, Cube.Move.R_, Cube.Move.U, Cube.Move.R, Cube.Move.F2]),
        ((Cube.LEFT, 2, 1), (Cube.DOWN, 1, 0), [Cube.Move.L2, Cube.Move.U_, Cube.Move.F2]),
        ((Cube.DOWN, 1, 0), (Cube.LEFT, 2, 1), [Cube.Move.L_, Cube.Move.F_, Cube.Move.L]),
        # Middle layer edges.
        ((Cube.FRONT, 1, 2), (Cube.RIGHT, 1, 0), [Cube.Move.F]),
        ((Cube.RIGHT, 1, 0), (Cube.FRONT, 1, 2), [Cube.Move.R, Cube.Move.U, Cube.Move.R_, Cube.Move.F2]),
        ((Cube.RIGHT, 1, 2), (Cube.BACK, 1, 0), [Cube.Move.R_, Cube.Move.U, Cube.Move.R, Cube.Move.F2]),
        ((Cube.BACK, 1, 0), (Cube.RIGHT, 1, 2), [Cube.Move.R2, Cube.Move.F, Cube.Move.R2]),
        ((Cube.BACK, 1, 2), (Cube.LEFT, 1, 0), [Cube.Move.B_, Cube.Move.U2, Cube.Move.B, Cube.Move.F2]),
        ((Cube.LEFT, 1, 0), (Cube.BACK, 1, 2), [Cube.Move.L, Cube.Move.U_, Cube.Move.L_, Cube.Move.F2]),
        ((Cube.LEFT, 1, 2), (Cube.FRONT, 1, 0), [Cube.Move.L_, Cube.Move.U_, Cube.Move.L, Cube.Move.F2]),
        ((Cube.FRONT, 1, 0), (Cube.LEFT, 1, 2), [Cube.Move.F_]),
        # Top edges.
        ((Cube.FRONT, 0, 1), (Cube.UP, 2, 1), [Cube.Move.F2]),
        ((Cube.UP, 2, 1), (Cube.FRONT, 0, 1), [Cube.Move.U_, Cube.Move.R_, Cube.Move.F, Cube.Move.R]),
        ((Cube.RIGHT, 0, 1), (Cube.UP, 1, 2), [Cube.Move.U, Cube.Move.F2]),
        ((Cube.UP, 1, 2), (Cube.RIGHT, 0, 1), [Cube.Move.R_, Cube.Move.F, Cube.Move.R]),
        ((Cube.BACK, 0, 1), (Cube.UP, 0, 1), [Cube.Move.U2, Cube.Move.F2]),
        ((Cube.UP, 0, 1), (Cube.BACK, 0, 1), [Cube.Move.U, Cube.Move.R_, Cube.Move.F, Cube.Move.R]),
        ((Cube.LEFT, 0, 1), (Cube.UP, 1, 0), [Cube.Move.U_, Cube.Move.F2]),
        ((Cube.UP, 1, 0), (Cube.LEFT, 0, 1), [Cube.Move.L, Cube.Move.F_, Cube.Move.L_]),
    ]

    def __createWhiteCross(self):
        for edgeColor in ['r', 'g', 'o', 'b']:
            for ((edgeFace, edgeRow, edgeCol), (whiteFace, whiteRow, whiteCol), movesList) in self.__whiteCrossMoves:
                if self.cube.cubeRepr[edgeFace][edgeRow][edgeCol] == edgeColor and self.cube.cubeRepr[whiteFace][whiteRow][whiteCol] == 'w':
                    for move in movesList:
                        self.cube.turn(move)
                    break
            self.cube.turn(Cube.Move.Y)

    def solve(self):
        self.__createWhiteCross()