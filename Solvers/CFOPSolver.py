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

        ((Cube.RIGHT, 2, 2), (Cube.BACK, 2, 0), (Cube.DOWN, 2, 2), [B, U, B_, U, R, U_, R_]),
        ((Cube.DOWN, 2, 2), (Cube.RIGHT, 2, 2), (Cube.BACK, 2, 0), [B, U, B_, R, U, R_]),
        ((Cube.BACK, 2, 0), (Cube.DOWN, 2, 2), (Cube.RIGHT, 2, 2), [R_, U2, R2, U_, R_]),

        ((Cube.BACK, 2, 2), (Cube.LEFT, 2, 0), (Cube.DOWN, 2, 0), [B_, U2, B, R, U, R_]),
        ((Cube.DOWN, 2, 0), (Cube.BACK, 2, 2), (Cube.LEFT, 2, 0), [L, U2, L_, R, U, R_]),
        ((Cube.LEFT, 2, 0), (Cube.DOWN, 2, 0), (Cube.BACK, 2, 2), [B_, U_, B, R, U_, R_]),

        ((Cube.LEFT, 2, 2), (Cube.FRONT, 2, 0), (Cube.DOWN, 0, 0), [L_, U_, L, R, U, R_]),
        ((Cube.DOWN, 0, 0), (Cube.LEFT, 2, 2), (Cube.FRONT, 2, 0), [F, U, F_, U2, R, U, R_]),
        ((Cube.FRONT, 2, 0), (Cube.DOWN, 0, 0), (Cube.LEFT, 2, 2), [L_, R, U_, R_, L]),

        ((Cube.FRONT, 0, 2), (Cube.UP, 2, 2), (Cube.RIGHT, 0, 0), [R, U, R_]),
        ((Cube.RIGHT, 0, 0), (Cube.FRONT, 0, 2), (Cube.UP, 2, 2), [R, U2, R_, U_, R, U, R_]),
        ((Cube.UP, 2, 2), (Cube.RIGHT, 0, 0), (Cube.FRONT, 0, 2), [U, R, U_, R_]),

        ((Cube.RIGHT, 0, 2), (Cube.UP, 0, 2), (Cube.BACK, 0, 0), [U, R, U, R_]),
        ((Cube.BACK, 0, 0), (Cube.RIGHT, 0, 2), (Cube.UP, 0, 2), [U, R, U2, R_, U_, R, U, R_]),
        ((Cube.UP, 0, 2), (Cube.BACK, 0, 0), (Cube.RIGHT, 0, 2), [U_, R, U2, R_]),

        ((Cube.BACK, 0, 2), (Cube.UP, 0, 0), (Cube.LEFT, 0, 0), [U2, R, U, R_]),
        ((Cube.LEFT, 0, 0), (Cube.BACK, 0, 2), (Cube.UP, 0, 0), [U2, R, U2, R_, U_, R, U, R_]),
        ((Cube.UP, 0, 0), (Cube.LEFT, 0, 0), (Cube.BACK, 0, 2), [R, U2, R_]),

        ((Cube.LEFT, 0, 2), (Cube.UP, 2, 0), (Cube.FRONT, 0, 0), [U_, R, U, R_]),
        ((Cube.FRONT, 0, 0), (Cube.LEFT, 0, 2), (Cube.UP, 2, 0), [U_, R, U2, R_, U_, R, U, R_]),
        ((Cube.UP, 2, 0), (Cube.FRONT, 0, 0), (Cube.LEFT, 0, 2), [R, U_, R_]),
    ]

    __middleLayerEdgesMoves = [
        ((Cube.FRONT, 1, 2), (Cube.RIGHT, 1, 0), []),
        ((Cube.RIGHT, 1, 0), (Cube.FRONT, 1, 2), [R, U, R_, U2, R, U2, R_, U, F_, U_, F]),

        ((Cube.RIGHT, 1, 2), (Cube.BACK, 1, 0), [R_, U, R, U, B, U_, B_, U,   R, U_, R_, U_, F_, U, F]),
        ((Cube.BACK, 1, 0), (Cube.RIGHT, 1, 2), [R_, U, R, U, B, U_, B_, U_,  U_, F_, U, F, U, R, U_, R_]),

        ((Cube.BACK, 1, 2), (Cube.LEFT, 1, 0), [L, U_, L_, U_, B_, U, B, U_,  U_, F_, U, F, U, R, U_, R_]),
        ((Cube.LEFT, 1, 0), (Cube.BACK, 1, 2), [L, U_, L_, U_, B_, U, B, U,   R, U_, R_, U_, F_, U, F]),

        ((Cube.FRONT, 1, 0), (Cube.LEFT, 1, 2), [L_, U, L, U, F, U_, F_, F_, U, F, U, R, U_, R_]),
        ((Cube.LEFT, 1, 2), (Cube.FRONT, 1, 0), [L_, U, L, U, F, U_, F_, U_, R, U_, R_, U_, F_, U, F]),

        ((Cube.FRONT, 0, 1), (Cube.UP, 2, 1), [U, R, U_, R_, U_, F_, U, F]),
        ((Cube.UP, 2, 1), (Cube.FRONT, 0, 1), [U2, F_, U, F, U, R, U_, R_]),

        ((Cube.RIGHT, 0, 1), (Cube.UP, 1, 2), [U2, R, U_, R_, U_, F_, U, F]),
        ((Cube.UP, 1, 2), (Cube.RIGHT, 0, 1), [U_, F_, U, F, U, R, U_, R_]),

        ((Cube.BACK, 0, 1), (Cube.UP, 0, 1), [U_, R, U_, R_, U_, F_, U, F]),
        ((Cube.UP, 0, 1), (Cube.BACK, 0, 1), [F_, U, F, U, R, U_, R_]),

        ((Cube.LEFT, 0, 1), (Cube.UP, 1, 0), [R, U_, R_, U_, F_, U, F]),
        ((Cube.UP, 1, 0), (Cube.LEFT, 0, 1), [U, F_, U, F, U, R, U_, R_])
    ]

    # The center is always yellow, so that's not included here.
    __OLLFirstLookMoves = [
        ([(Cube.UP, 0, 1), (Cube.UP, 1, 0), (Cube.UP, 1, 2), (Cube.UP, 2, 1)], []),
        ([(Cube.BACK, 0, 1), (Cube.LEFT, 0, 1), (Cube.UP, 1, 2), (Cube.UP, 2, 1)], [B, U, L, U_, L_, B_]),
        ([(Cube.BACK, 0, 1), (Cube.UP, 1, 0), (Cube.UP, 1, 2), (Cube.FRONT, 0, 1)], [F, R, U, R_, U_, F_]),
        ([(Cube.BACK, 0, 1), (Cube.LEFT, 0, 1), (Cube.RIGHT, 0, 1), (Cube.FRONT, 0, 1)], [F, R, U, R_, U_, F_, B, U, L, U_, L_, B_])
    ]

    # The cross is already yellow, so that's not included here.
    __OLLSecondLookMoves = [
        ([(Cube.UP, 0, 0), (Cube.UP, 0, 2), (Cube.UP, 2, 0), (Cube.UP, 2, 2)], []),
        ([(Cube.BACK, 0, 2), (Cube.RIGHT, 0, 2), (Cube.FRONT, 0, 2), (Cube.UP, 2, 0)], [R, U, R_, U, R, U2, R_]),
        ([(Cube.BACK, 0, 0), (Cube.LEFT, 0, 0), (Cube.LEFT, 0, 2), (Cube.FRONT, 0, 2)], [R, U2, R2, U_, R2, U_, R2, U2, R]),
        ([(Cube.BACK, 0, 2), (Cube.FRONT, 0, 0), (Cube.UP, 0, 2), (Cube.UP, 2, 2)], [L, F, R_, F_, L_, F, R, F_]),
        ([(Cube.FRONT, 0, 0), (Cube.FRONT, 0, 2), (Cube.UP, 0, 0), (Cube.UP, 0, 2)], [R2, D, R_, U2, R, D_, R_, U2, R_]),
        ([(Cube.UP, 0, 2), (Cube.LEFT, 0, 0), (Cube.FRONT, 0, 0), (Cube.RIGHT, 0, 0)], [R, U2, R_, U_, R, U_, R_]),
        ([(Cube.BACK, 0, 2), (Cube.BACK, 0, 0), (Cube.FRONT, 0, 0), (Cube.FRONT, 0, 2)], [F, R, U, R_, U_, R, U, R_, U_, R, U, R_, U_, F_]),
        ([(Cube.UP, 0, 2), (Cube.UP, 2, 0), (Cube.LEFT, 0, 0), (Cube.FRONT, 0, 2)], [F_, L, F, R_, F_, L_, F, R])
    ]

    def __createWhiteCross(self):
        for edgeColor in ['r', 'g', 'o', 'b']:
            for ((edgeFace, edgeRow, edgeCol), (whiteFace, whiteRow, whiteCol), movesList) in self.__whiteCrossMoves:
                if self.cube.cubeRepr[edgeFace][edgeRow][edgeCol] == edgeColor and \
                        self.cube.cubeRepr[whiteFace][whiteRow][whiteCol] == 'w': # This color is always white since it's for the bottom layer.
                    for move in movesList:
                        self.cube.turn(move)
                    break
            self.cube.turn(Y)

    def __placeBottomLayerCorners(self):
        for (frontCornerColor, rightCornerColor) in [('r', 'g'), ('g', 'o'), ('o', 'b'), ('b', 'r')]:
            for ((frontFace, frontRow, frontCol), (rightFace, rightRow, rightCol), (downFace, downRow, downCol), movesList) in self.__bottomLayerCornersMoves:
                if self.cube.cubeRepr[frontFace][frontRow][frontCol] == frontCornerColor and \
                        self.cube.cubeRepr[rightFace][rightRow][rightCol] == rightCornerColor and \
                        self.cube.cubeRepr[downFace][downRow][downCol] == 'w': # This color is always white since it's for the bottom layer.
                    for move in movesList:
                        self.cube.turn(move)
                    break
            self.cube.turn(Y)

    def __placeMiddleLayerEdges(self):
        for (edgeFrontColor, edgeRightColor) in [('r', 'g'), ('g', 'o'), ('o', 'b'), ('b', 'r')]:
            for ((edgeFace, edgeRow, edgeCol), (whiteFace, whiteRow, whiteCol), movesList) in self.__middleLayerEdgesMoves:
                if self.cube.cubeRepr[edgeFace][edgeRow][edgeCol] == edgeFrontColor and \
                        self.cube.cubeRepr[whiteFace][whiteRow][whiteCol] == edgeRightColor:
                    for move in movesList:
                        self.cube.turn(move)
                    break
            self.cube.turn(Y)

    def __orientLastLayer(self):
        # This order is essential, otherwise it won't work.
        for patterns in [self.__OLLFirstLookMoves, self.__OLLSecondLookMoves]:
            currentOLLStepDone = False # Flag for the whole step's status.
            while(not currentOLLStepDone):
                for (yellowCoords, movesList) in patterns:
                    patternFound = True # Flag for whether the current pattern is satisified or not.
                    # Check if listed coords are all yellow.
                    for (yellowFace, yellowRow, yellowCol) in yellowCoords:
                        if self.cube.cubeRepr[yellowFace][yellowRow][yellowCol] != 'y':
                            patternFound = False
                            break
                    # If they are, perform the moves, restore the cube, then return.
                    if patternFound:
                        for move in movesList:
                            self.cube.turn(move)
                        currentOLLStepDone = True
                        break
                    # Else, continue checking the other patterns.
                # If none of the patterns match, that means the cube isn't oriented correctly. Do a Y rotation and try again.
                self.cube.turn(Y)
        
        # Rotate the cube so that red is front again.
        while (self.cube.cubeRepr[Cube.FRONT][1][1] != 'r'):
            self.cube.turn(Y)

    def __permuteLastLayer(self):
        # Keep repeating algo until a single pair of headlights appears.
        headlightColor = ''
        while headlightColor == '':
            # Check the headlight cells of each layer to see if any exist at all.
            if self.cube.cubeRepr[Cube.FRONT][0][0] == self.cube.cubeRepr[Cube.FRONT][0][2]:
                headlightColor = self.cube.cubeRepr[Cube.FRONT][0][0]
            elif self.cube.cubeRepr[Cube.RIGHT][0][0] == self.cube.cubeRepr[Cube.RIGHT][0][2]:
                headlightColor = self.cube.cubeRepr[Cube.RIGHT][0][0]
            elif self.cube.cubeRepr[Cube.BACK][0][0] == self.cube.cubeRepr[Cube.BACK][0][2]:
                headlightColor = self.cube.cubeRepr[Cube.BACK][0][0]
            elif self.cube.cubeRepr[Cube.LEFT][0][0] == self.cube.cubeRepr[Cube.LEFT][0][2]:
                headlightColor = self.cube.cubeRepr[Cube.LEFT][0][0]
            else:
                for move in [R_, F, R_, B2, R, F_, R_, B2, R2]:
                    self.cube.turn(move)

        # Move the headlights to the back and repeat the algo until all corners are lined up.
        while self.cube.cubeRepr[Cube.BACK][0][0] != headlightColor and self.cube.cubeRepr[Cube.BACK][0][2] != headlightColor:
            self.cube.turn(U)
        while not (self.cube.cubeRepr[Cube.FRONT][0][0] == self.cube.cubeRepr[Cube.FRONT][0][2] and \
                self.cube.cubeRepr[Cube.RIGHT][0][0] == self.cube.cubeRepr[Cube.RIGHT][0][2] and \
                self.cube.cubeRepr[Cube.BACK][0][0] == self.cube.cubeRepr[Cube.BACK][0][2] and \
                self.cube.cubeRepr[Cube.LEFT][0][0] == self.cube.cubeRepr[Cube.LEFT][0][2]):
            for move in [R_, F, R_, B2, R, F_, R_, B2, R2]:
                self.cube.turn(move)
        
        # Now, keep repeating the algo until we create a solved edge.
        solvedEdgeColor = ''
        while solvedEdgeColor == '':
            if self.cube.cubeRepr[Cube.FRONT][0][0] == self.cube.cubeRepr[Cube.FRONT][0][1] == self.cube.cubeRepr[Cube.FRONT][0][2]:
                solvedEdgeColor = self.cube.cubeRepr[Cube.FRONT][0][0]
            elif self.cube.cubeRepr[Cube.RIGHT][0][0] == self.cube.cubeRepr[Cube.RIGHT][0][1] == self.cube.cubeRepr[Cube.RIGHT][0][2]:
                solvedEdgeColor = self.cube.cubeRepr[Cube.RIGHT][0][0]
            elif self.cube.cubeRepr[Cube.BACK][0][0] == self.cube.cubeRepr[Cube.BACK][0][1] == self.cube.cubeRepr[Cube.BACK][0][2]:
                solvedEdgeColor = self.cube.cubeRepr[Cube.BACK][0][0]
            elif self.cube.cubeRepr[Cube.LEFT][0][0] == self.cube.cubeRepr[Cube.LEFT][0][1] == self.cube.cubeRepr[Cube.LEFT][0][2]:
                solvedEdgeColor = self.cube.cubeRepr[Cube.LEFT][0][0]
            else:
                for move in [R, U_, R, U, R, U, R, U_, R_, U_, R2]:
                    self.cube.turn(move)
                
        # Move the solved edge to the back and finish this.
        while self.cube.cubeRepr[Cube.BACK][0][1] != solvedEdgeColor:
            self.cube.turn(U)
        while self.cube.cubeRepr[Cube.FRONT][0][0] != self.cube.cubeRepr[Cube.FRONT][0][1]:
            for move in [R, U_, R, U, R, U, R, U_, R_, U_, R2]:
                self.cube.turn(move)

        # At this point, the top layer is solved. We only need to rotate it until it lines up correctly with the centers.
        while self.cube.cubeRepr[Cube.FRONT][0][0] != 'r':
            self.cube.turn(U)
            

    def solve(self):
        self.__createWhiteCross()
        self.__placeBottomLayerCorners()
        self.__placeMiddleLayerEdges()
        self.__orientLastLayer()
        self.__permuteLastLayer()
