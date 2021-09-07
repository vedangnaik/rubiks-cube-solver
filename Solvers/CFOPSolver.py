from Solvers.Solver import Solver
from Cube.Cube import Cube
from Cube.Move import *


class CFOPSolver(Solver):
    __whiteCrossMoves = [
        # Bottom layer edges.
        ((Cube.FRONT, 2, 1), (Cube.DOWN, 0, 1), []),
        ((Cube.DOWN, 0, 1), (Cube.FRONT, 2, 1), [F_, D, R_, D_]),
        ((Cube.RIGHT, 2, 1), (Cube.DOWN, 1, 2), [R2, U, F2]),
        ((Cube.DOWN, 1, 2), (Cube.RIGHT, 2, 1), [R, F]),
        ((Cube.BACK, 2, 1), (Cube.DOWN, 2, 1), [B2, U2, F2]),
        ((Cube.DOWN, 2, 1), (Cube.BACK, 2, 1), [B, R_, U, R, F2]),
        ((Cube.LEFT, 2, 1), (Cube.DOWN, 1, 0), [L2, U_, F2]),
        ((Cube.DOWN, 1, 0), (Cube.LEFT, 2, 1), [L_, F_, L]),
        # Middle layer edges.
        ((Cube.FRONT, 1, 2), (Cube.RIGHT, 1, 0), [F]),
        ((Cube.RIGHT, 1, 0), (Cube.FRONT, 1, 2), [R, U, R_, F2]),
        ((Cube.RIGHT, 1, 2), (Cube.BACK, 1, 0), [R_, U, R, F2]),
        ((Cube.BACK, 1, 0), (Cube.RIGHT, 1, 2), [R2, F, R2]),
        ((Cube.BACK, 1, 2), (Cube.LEFT, 1, 0), [B_, U2, B, F2]),
        ((Cube.LEFT, 1, 0), (Cube.BACK, 1, 2), [L, U_, L_, F2]),
        ((Cube.LEFT, 1, 2), (Cube.FRONT, 1, 0), [L_, U_, L, F2]),
        ((Cube.FRONT, 1, 0), (Cube.LEFT, 1, 2), [F_]),
        # Top edges.
        ((Cube.FRONT, 0, 1), (Cube.UP, 2, 1), [F2]),
        ((Cube.UP, 2, 1), (Cube.FRONT, 0, 1), [U_, R_, F, R]),
        ((Cube.RIGHT, 0, 1), (Cube.UP, 1, 2), [U, F2]),
        ((Cube.UP, 1, 2), (Cube.RIGHT, 0, 1), [R_, F, R]),
        ((Cube.BACK, 0, 1), (Cube.UP, 0, 1), [U2, F2]),
        ((Cube.UP, 0, 1), (Cube.BACK, 0, 1), [U, R_, F, R]),
        ((Cube.LEFT, 0, 1), (Cube.UP, 1, 0), [U_, F2]),
        ((Cube.UP, 1, 0), (Cube.LEFT, 0, 1), [L, F_, L_]),
    ]

    __bottomLayerCornersMoves = [
        ((Cube.FRONT, 2, 2), (Cube.RIGHT, 2, 0), (Cube.DOWN, 0, 2), []),
        ((Cube.DOWN, 0, 2), (Cube.FRONT, 2, 2), (Cube.RIGHT, 2, 0), [R, U, R_, U_, R, U, R_]),
        ((Cube.RIGHT, 2, 0), (Cube.DOWN, 0, 2), (Cube.FRONT, 2, 2), [R, U_, R_, U, R, U_, R_]),

        ((Cube.RIGHT, 2, 2), (Cube.BACK, 2, 0), (Cube.DOWN, 2, 2), [R]),
    ]

    def __createWhiteCross(self):
        for edgeColor in ['r', 'g', 'o', 'b']:
            for ((edgeFace, edgeRow, edgeCol), (whiteFace, whiteRow, whiteCol), movesList) in self.__whiteCrossMoves:
                if self.cube.cubeRepr[edgeFace][edgeRow][edgeCol] == edgeColor and self.cube.cubeRepr[whiteFace][whiteRow][whiteCol] == 'w':
                    for move in movesList:
                        self.cube.turn(move)
                    break
            self.cube.turn(Y)

    def __placeBottomLayerCorners(self):
        for (frontCornerColor, rightCornerColor) in [('r', 'g')]:
            for ((frontFace, frontRow, frontCol), (rightFace, rightRow, rightCol), (downFace, downRow, downCol), movesList) in self.__bottomLayerCornersMoves:
                if self.cube.cubeRepr[frontFace][frontRow][frontCol] == frontCornerColor and \
                        self.cube.cubeRepr[rightFace][rightRow][rightCol] == rightCornerColor and \
                        self.cube.cubeRepr[downFace][downRow][downCol] == 'w':
                    for move in movesList:
                        self.cube.turn(move)
                    break
            # self.cube.turn(Y)


    def solve(self):
        self.__createWhiteCross()
        # self.__placeBottomLayerCorners()