from colorama import Back, init, Fore
from enum import Enum

class Cube:
    # Map of cube colours to codes for colorama.
    __colorMap = {
        'r': Back.RED,
        'g': Back.GREEN,
        'o': Back.MAGENTA, # No orange :(
        'b': Back.BLUE,
        'y': Back.YELLOW,
        'w': Back.WHITE,
    }

    # Enum of the 18 cube moves.
    class Move(Enum):
        F = 1
        F_ = 2
        F2 = 3
        R = 4
        R_ = 5
        R2 = 6
        B = 7
        B_ = 8
        B2 = 9
        L = 10
        L_ = 11
        L2 = 12
        U = 13
        U_ = 14
        U2 = 15
        D = 16
        D_ = 17
        D2 = 18

    # Direction enum mainly for self.__rotateFace. Normal = clockwise, Prime = anticlockwise, OneEighty = half-turn.
    class __Direction(Enum):
        Normal = 1
        Prime = 2
        OneEighty = 3

    # Axis anum mainly for self.__flipCubeAcrossAxis. Axis name indicates the faces that axis goes through.
    class __Axis(Enum):
        UP_DOWN = 1
        RIGHT_LEFT = 2
        FRONT_BACK = 3

    # Face numbers. An enum is too inconvenient since we only need the numbers.
    FRONT = 0
    RIGHT = 1
    BACK = 2
    LEFT = 3
    UP = 4
    DOWN = 5

    # Flips cubes (i.e. rotates 180 degrees) about given axis. Mainly used to exploit symmetries and reuse code in self.turn.
    def __flipCubeAcrossAxis(self, axis):
        if axis == Cube.__Axis.UP_DOWN:
            # First, swap FRONT-BACK and RIGHT-LEFT
            self.cubeRepr[Cube.FRONT], self.cubeRepr[Cube.BACK] = self.cubeRepr[Cube.BACK], self.cubeRepr[Cube.FRONT]
            self.cubeRepr[Cube.RIGHT], self.cubeRepr[Cube.LEFT] = self.cubeRepr[Cube.LEFT], self.cubeRepr[Cube.RIGHT]
            # Then, 180 rotate UP and DOWN.
            self.__rotateFace(self.cubeRepr[Cube.UP], Cube.__Direction.OneEighty)
            self.__rotateFace(self.cubeRepr[Cube.DOWN], Cube.__Direction.OneEighty)
        elif axis == Cube.__Axis.RIGHT_LEFT:
            # First, swap UP-DOWN
            self.cubeRepr[Cube.UP], self.cubeRepr[Cube.DOWN] = self.cubeRepr[Cube.DOWN], self.cubeRepr[Cube.UP]
            # Then, swap FRONT-BACK and rotate both by 180 - In this coordinate system, FRONT and BACK are only symmetric about UP_DOWN, not RIGHT_LEFT.
            self.cubeRepr[Cube.FRONT], self.cubeRepr[Cube.BACK] = self.cubeRepr[Cube.BACK], self.cubeRepr[Cube.FRONT]
            self.__rotateFace(self.cubeRepr[Cube.FRONT], Cube.__Direction.OneEighty)
            self.__rotateFace(self.cubeRepr[Cube.BACK], Cube.__Direction.OneEighty)
            # Then, 180 rotate RIGHT and LEFT.
            self.__rotateFace(self.cubeRepr[Cube.RIGHT], Cube.__Direction.OneEighty)
            self.__rotateFace(self.cubeRepr[Cube.LEFT], Cube.__Direction.OneEighty)
        elif axis == Cube.__Axis.FRONT_BACK:
            print("FRONT_BACK is an unused flip axis.")

    # Rotates face colors only (not edge/corner colors) for the given face in the given direction.
    def __rotateFace(self, face, dir):
        if dir == Cube.__Direction.Normal:
            # Rotate corners, then edges. The center is fixed.
            face[0][0], face[0][2], face[2][2], face[2][0] = face[2][0], face[0][0], face[0][2], face[2][2]
            face[1][0], face[0][1], face[1][2], face[2][1] = face[2][1], face[1][0], face[0][1], face[1][2]
        elif dir == Cube.__Direction.Prime:
            face[0][0], face[0][2], face[2][2], face[2][0] = face[0][2], face[2][2], face[2][0], face[0][0]
            face[1][0], face[0][1], face[1][2], face[2][1] = face[0][1], face[1][2], face[2][1], face[1][0]
        elif dir == Cube.__Direction.OneEighty:
            # Flip opposite corners.
            face[0][0], face[2][2] = face[2][2], face[0][0]
            face[0][2], face[2][0] = face[2][0], face[0][2]
            # Flip opposite edges.
            face[1][0], face[1][2] = face[1][2], face[1][0]
            face[0][1], face[2][1] = face[2][1], face[0][1]

    # Main function which implement the cube moves. Probably can be cleaned up more with the bitboard representation, but it's fine for now.
    def turn(self, move):
        if move == Cube.Move.F:
            self.__rotateFace(self.cubeRepr[Cube.FRONT], Cube.__Direction.Normal)
            self.cubeRepr[Cube.LEFT][2][2], self.cubeRepr[Cube.UP][2][0], self.cubeRepr[Cube.RIGHT][0][0], self.cubeRepr[Cube.DOWN][0][2] = self.cubeRepr[Cube.DOWN][0][2], self.cubeRepr[Cube.LEFT][2][2], self.cubeRepr[Cube.UP][2][0], self.cubeRepr[Cube.RIGHT][0][0]
            self.cubeRepr[Cube.LEFT][1][2], self.cubeRepr[Cube.UP][2][1], self.cubeRepr[Cube.RIGHT][1][0], self.cubeRepr[Cube.DOWN][0][1] = self.cubeRepr[Cube.DOWN][0][1], self.cubeRepr[Cube.LEFT][1][2], self.cubeRepr[Cube.UP][2][1], self.cubeRepr[Cube.RIGHT][1][0]
            self.cubeRepr[Cube.LEFT][0][2], self.cubeRepr[Cube.UP][2][2], self.cubeRepr[Cube.RIGHT][2][0], self.cubeRepr[Cube.DOWN][0][0] = self.cubeRepr[Cube.DOWN][0][0], self.cubeRepr[Cube.LEFT][0][2], self.cubeRepr[Cube.UP][2][2], self.cubeRepr[Cube.RIGHT][2][0]

        # Take advantage of FRONT-BACK symmetry to reuse the F code. See code for L.
        elif move == Cube.Move.B:
            self.__flipCubeAcrossAxis(Cube.__Axis.UP_DOWN)
            self.turn(Cube.Move.F)
            self.__flipCubeAcrossAxis(Cube.__Axis.UP_DOWN)

        elif move == Cube.Move.R:
            self.__rotateFace(self.cubeRepr[Cube.RIGHT], Cube.__Direction.Normal)
            self.cubeRepr[Cube.FRONT][2][2], self.cubeRepr[Cube.UP][2][2], self.cubeRepr[Cube.BACK][0][0], self.cubeRepr[Cube.DOWN][2][2] = self.cubeRepr[Cube.DOWN][2][2], self.cubeRepr[Cube.FRONT][2][2], self.cubeRepr[Cube.UP][2][2], self.cubeRepr[Cube.BACK][0][0]
            self.cubeRepr[Cube.FRONT][1][2], self.cubeRepr[Cube.UP][1][2], self.cubeRepr[Cube.BACK][1][0], self.cubeRepr[Cube.DOWN][1][2] = self.cubeRepr[Cube.DOWN][1][2], self.cubeRepr[Cube.FRONT][1][2], self.cubeRepr[Cube.UP][1][2], self.cubeRepr[Cube.BACK][1][0]
            self.cubeRepr[Cube.FRONT][0][2], self.cubeRepr[Cube.UP][0][2], self.cubeRepr[Cube.BACK][2][0], self.cubeRepr[Cube.DOWN][0][2] = self.cubeRepr[Cube.DOWN][0][2], self.cubeRepr[Cube.FRONT][0][2], self.cubeRepr[Cube.UP][0][2], self.cubeRepr[Cube.BACK][2][0]

        # Take advantage of RIGHT-LEFT symmetry to reuse the R code.
        elif move == Cube.Move.L:
            # Rotate the cube 180 degrees around the UP-DOWN axis.
            self.__flipCubeAcrossAxis(Cube.__Axis.UP_DOWN)
            # Now, do the normal right rotation. This is just one level of recursion.
            self.turn(Cube.Move.R)
            # Undo the flip by flipping again
            self.__flipCubeAcrossAxis(Cube.__Axis.UP_DOWN)

        # Since this goes across the rows, we can exploit whole-row swapping to keep this clean.
        elif move == Cube.Move.U:
            self.__rotateFace(self.cubeRepr[Cube.UP], Cube.__Direction.Normal)
            self.cubeRepr[Cube.FRONT][0][:], self.cubeRepr[Cube.LEFT][0][:], self.cubeRepr[Cube.BACK][0][:], self.cubeRepr[Cube.RIGHT][0][:] = self.cubeRepr[Cube.RIGHT][0][:], self.cubeRepr[Cube.FRONT][0][:], self.cubeRepr[Cube.LEFT][0][:], self.cubeRepr[Cube.BACK][0][:]
        
        # Take advantage of RIGHT-LEFT symmetry to reuse the U code. See code for L.
        elif move == Cube.Move.D:
            self.__flipCubeAcrossAxis(Cube.__Axis.RIGHT_LEFT)
            self.turn(Cube.Move.U)
            self.__flipCubeAcrossAxis(Cube.__Axis.RIGHT_LEFT)

        if move == Cube.Move.F_:
            self.__rotateFace(self.cubeRepr[Cube.FRONT], Cube.__Direction.Prime)
            self.cubeRepr[Cube.LEFT][2][2], self.cubeRepr[Cube.UP][2][0], self.cubeRepr[Cube.RIGHT][0][0], self.cubeRepr[Cube.DOWN][0][2] = self.cubeRepr[Cube.UP][2][0], self.cubeRepr[Cube.RIGHT][0][0], self.cubeRepr[Cube.DOWN][0][2], self.cubeRepr[Cube.LEFT][2][2]
            self.cubeRepr[Cube.LEFT][1][2], self.cubeRepr[Cube.UP][2][1], self.cubeRepr[Cube.RIGHT][1][0], self.cubeRepr[Cube.DOWN][0][1] = self.cubeRepr[Cube.UP][2][1], self.cubeRepr[Cube.RIGHT][1][0], self.cubeRepr[Cube.DOWN][0][1], self.cubeRepr[Cube.LEFT][1][2]
            self.cubeRepr[Cube.LEFT][0][2], self.cubeRepr[Cube.UP][2][2], self.cubeRepr[Cube.RIGHT][2][0], self.cubeRepr[Cube.DOWN][0][0] = self.cubeRepr[Cube.UP][2][2], self.cubeRepr[Cube.RIGHT][2][0], self.cubeRepr[Cube.DOWN][0][0], self.cubeRepr[Cube.LEFT][0][2]

        # Take advantage of FRONT-BACK symmetry to reuse the F_ code. See code for L.
        elif move == Cube.Move.B_:
            self.__flipCubeAcrossAxis(Cube.__Axis.UP_DOWN)
            self.turn(Cube.Move.F_)
            self.__flipCubeAcrossAxis(Cube.__Axis.UP_DOWN)

        elif move == Cube.Move.R_:
            self.__rotateFace(self.cubeRepr[Cube.RIGHT], Cube.__Direction.Prime)
            self.cubeRepr[Cube.FRONT][2][2], self.cubeRepr[Cube.UP][2][2], self.cubeRepr[Cube.BACK][0][0], self.cubeRepr[Cube.DOWN][2][2] = self.cubeRepr[Cube.UP][2][2], self.cubeRepr[Cube.BACK][0][0], self.cubeRepr[Cube.DOWN][2][2], self.cubeRepr[Cube.FRONT][2][2]
            self.cubeRepr[Cube.FRONT][1][2], self.cubeRepr[Cube.UP][1][2], self.cubeRepr[Cube.BACK][1][0], self.cubeRepr[Cube.DOWN][1][2] = self.cubeRepr[Cube.UP][1][2], self.cubeRepr[Cube.BACK][1][0], self.cubeRepr[Cube.DOWN][1][2], self.cubeRepr[Cube.FRONT][1][2]
            self.cubeRepr[Cube.FRONT][0][2], self.cubeRepr[Cube.UP][0][2], self.cubeRepr[Cube.BACK][2][0], self.cubeRepr[Cube.DOWN][0][2] = self.cubeRepr[Cube.UP][0][2], self.cubeRepr[Cube.BACK][2][0], self.cubeRepr[Cube.DOWN][0][2], self.cubeRepr[Cube.FRONT][0][2]

        # Take advantage of RIGHT-LEFT symmetry to reuse the R_ code. See code for L.
        elif move == Cube.Move.L_:
            self.__flipCubeAcrossAxis(Cube.__Axis.UP_DOWN)
            self.turn(Cube.Move.R_)
            self.__flipCubeAcrossAxis(Cube.__Axis.UP_DOWN)

        elif move == Cube.Move.U_:
            self.__rotateFace(self.cubeRepr[Cube.UP], Cube.__Direction.Prime)
            self.cubeRepr[Cube.FRONT][0][:], self.cubeRepr[Cube.LEFT][0][:], self.cubeRepr[Cube.BACK][0][:], self.cubeRepr[Cube.RIGHT][0][:] = self.cubeRepr[Cube.LEFT][0][:], self.cubeRepr[Cube.BACK][0][:], self.cubeRepr[Cube.RIGHT][0][:], self.cubeRepr[Cube.FRONT][0][:]
        
        # Take advantage of RIGHT-LEFT symmetry to reuse the U_ code. See code for L.
        elif move == Cube.Move.D_:
            self.__flipCubeAcrossAxis(Cube.__Axis.RIGHT_LEFT)
            self.turn(Cube.Move.U_)
            self.__flipCubeAcrossAxis(Cube.__Axis.RIGHT_LEFT)

        # Just do the base move two times.
        elif move == Cube.Move.F2:
            self.turn(Cube.Move.F)
            self.turn(Cube.Move.F)

        elif move == Cube.Move.B2:
            self.turn(Cube.Move.B)
            self.turn(Cube.Move.B)

        elif move == Cube.Move.R2:
            self.turn(Cube.Move.R)
            self.turn(Cube.Move.R)

        elif move == Cube.Move.L2:
            self.turn(Cube.Move.L)
            self.turn(Cube.Move.L)

        elif move == Cube.Move.U2:
            self.turn(Cube.Move.U)
            self.turn(Cube.Move.U)

        elif move == Cube.Move.D2:
            self.turn(Cube.Move.D)
            self.turn(Cube.Move.D)

    # Prints a colored 'net' of the cube. See https://ell.stackexchange.com/questions/222545/what-is-this-opened-cube-called for what that means. Orange is not available in colorama, so magenta is used instead.
    def draw(self):
        print()

        # Full U face.
        for row in range(3):
            print(13 * " ", end="")
            for col in range(3):
                cell = self.cubeRepr[Cube.UP][row][col]
                print(f" {Fore.BLACK}{self.__colorMap[cell]}{row}{col}", end="")
            print(" ")
        print()

        # First row of L, F, R, B faces
        for row in range(3):
            print("| ", end="")
            for face in [Cube.LEFT, Cube.FRONT, Cube.RIGHT, Cube.BACK]:
                for col in range(3):
                    cell = self.cubeRepr[face][row][col]
                    print(f" {Fore.BLACK}{self.__colorMap[cell]}{row}{col}", end="")
                print(" |", end="")
            print()
        print()

        # Full D face.
        for row in range(3):
            print(13 * " ", end="")
            for col in range(3):
                cell = self.cubeRepr[Cube.DOWN][row][col]
                print(f" {Fore.BLACK}{self.__colorMap[cell]}{row}{col}", end="")
            print(" ")
        print()
        print()

    # Constructor. Sets up the initial state as the cube being solved, with F = red face, U = yellow face, and D = white face.
    def __init__(self):
        self.cubeRepr = [
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



whiteCrossMoves = [
    ((Cube.FRONT, 2, 1), (Cube.DOWN, 0, 1), []),
    ((Cube.DOWN, 0, 1), (Cube.FRONT, 2, 1), [Cube.Move.F_, Cube.Move.D, Cube.Move.R_, Cube.Move.D_])
]


if __name__ == "__main__":
    import random
    init(autoreset=True)

    a = Cube()

    print("Starting:")
    a.draw()

    print("Scrambling:")    
    moves = [Cube.Move.D, Cube.Move.R, Cube.Move.D_, Cube.Move.F]
    for move in moves:
        a.turn(move)
    a.draw()

    print("White cross: ")
    for ((redFace, redRow, redCol), (whiteFace, whiteRow, whiteCol), movesList) in whiteCrossMoves:
        if a.cubeRepr[redFace][redRow][redCol] == 'r' and a.cubeRepr[whiteFace][whiteRow][whiteCol] == 'w':
            for move in movesList:
                a.turn(move)
    a.draw()