from colorama import Back, init, Style, Fore
from enum import Enum

from colorama.initialise import reset_all

class Cube:
    __colorMapping = {
        'r': Back.RED,
        'g': Back.GREEN,
        'o': Back.MAGENTA, # No orange :(
        'b': Back.BLUE,
        'y': Back.YELLOW,
        'w': Back.WHITE,
    }

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

    class __Direction(Enum):
        Normal = 1
        Prime = 2
        OneEighty = 3

    class __Axis(Enum):
        UP_DOWN = 1
        RIGHT_LEFT = 2
        FRONT_BACK = 3

    # Face numbers. An enum is too inconvenient.
    __FRONT = 0
    __RIGHT = 1
    __BACK = 2
    __LEFT = 3
    __UP = 4
    __DOWN = 5


    def __flipCubeAcrossAxis(self, axis):
        if axis == Cube.__Axis.UP_DOWN:
            # First, swap FRONT-BACK and RIGHT-LEFT
            self.__cubeRepr[Cube.__FRONT], self.__cubeRepr[Cube.__BACK] = self.__cubeRepr[Cube.__BACK], self.__cubeRepr[Cube.__FRONT]
            self.__cubeRepr[Cube.__RIGHT], self.__cubeRepr[Cube.__LEFT] = self.__cubeRepr[Cube.__LEFT], self.__cubeRepr[Cube.__RIGHT]
            # Then, 180 rotate UP and DOWN.
            self.__rotateFace(self.__cubeRepr[Cube.__UP], Cube.__Direction.OneEighty)
            self.__rotateFace(self.__cubeRepr[Cube.__DOWN], Cube.__Direction.OneEighty)

        elif axis == Cube.__Axis.RIGHT_LEFT:
            pass
        elif axis == Cube.__Axis.FRONT_BACK:
            pass


    def __rotateFace(self, face, dir):
        if dir == Cube.__Direction.Normal:
            # Rotate corners, then edges. The center is fixed.
            face[0][0], face[0][2], face[2][2], face[2][0] = face[2][0], face[0][0], face[0][2], face[2][2]
            face[1][0], face[0][1], face[1][2], face[2][1] = face[2][1], face[1][0], face[0][1], face[1][2]
        elif dir == Cube.__Direction.Prime:
            pass
        elif dir == Cube.__Direction.OneEighty:
            # Flip opposite corners.
            face[0][0], face[2][2] = face[2][2], face[0][0]
            face[0][2], face[2][0] = face[2][0], face[0][2]
            # Flip opposite edges.
            face[1][0], face[1][2] = face[1][2], face[1][0]
            face[0][1], face[2][1] = face[2][1], face[0][1]

    def turn(self, move):
        if move == Cube.Move.F:
            self.__rotateFace(self.__cubeRepr[Cube.__FRONT], Cube.__Direction.Normal)
            # Rotate 
            self.__cubeRepr[Cube.__LEFT][2][2], self.__cubeRepr[Cube.__UP][2][0], self.__cubeRepr[Cube.__RIGHT][0][0], self.__cubeRepr[Cube.__DOWN][0][2] = self.__cubeRepr[Cube.__DOWN][0][2], self.__cubeRepr[Cube.__LEFT][2][2], self.__cubeRepr[Cube.__UP][2][0], self.__cubeRepr[Cube.__RIGHT][0][0]
            self.__cubeRepr[Cube.__LEFT][1][2], self.__cubeRepr[Cube.__UP][2][1], self.__cubeRepr[Cube.__RIGHT][1][0], self.__cubeRepr[Cube.__DOWN][0][1] = self.__cubeRepr[Cube.__DOWN][0][1], self.__cubeRepr[Cube.__LEFT][1][2], self.__cubeRepr[Cube.__UP][2][1], self.__cubeRepr[Cube.__RIGHT][1][0]
            self.__cubeRepr[Cube.__LEFT][0][2], self.__cubeRepr[Cube.__UP][2][2], self.__cubeRepr[Cube.__RIGHT][2][0], self.__cubeRepr[Cube.__DOWN][0][0] = self.__cubeRepr[Cube.__DOWN][0][0], self.__cubeRepr[Cube.__LEFT][0][2], self.__cubeRepr[Cube.__UP][2][2], self.__cubeRepr[Cube.__RIGHT][2][0]

        elif move == Cube.Move.R:
            self.__rotateFace(self.__cubeRepr[Cube.__RIGHT], Cube.__Direction.Normal)
            self.__cubeRepr[Cube.__FRONT][2][2], self.__cubeRepr[Cube.__UP][2][2], self.__cubeRepr[Cube.__BACK][0][0], self.__cubeRepr[Cube.__DOWN][2][2] = self.__cubeRepr[Cube.__DOWN][2][2], self.__cubeRepr[Cube.__FRONT][2][2], self.__cubeRepr[Cube.__UP][2][2], self.__cubeRepr[Cube.__BACK][0][0]
            self.__cubeRepr[Cube.__FRONT][1][2], self.__cubeRepr[Cube.__UP][1][2], self.__cubeRepr[Cube.__BACK][1][0], self.__cubeRepr[Cube.__DOWN][1][2] = self.__cubeRepr[Cube.__DOWN][1][2], self.__cubeRepr[Cube.__FRONT][1][2], self.__cubeRepr[Cube.__UP][1][2], self.__cubeRepr[Cube.__BACK][1][0]
            self.__cubeRepr[Cube.__FRONT][0][2], self.__cubeRepr[Cube.__UP][0][2], self.__cubeRepr[Cube.__BACK][2][0], self.__cubeRepr[Cube.__DOWN][0][2] = self.__cubeRepr[Cube.__DOWN][0][2], self.__cubeRepr[Cube.__FRONT][0][2], self.__cubeRepr[Cube.__UP][0][2], self.__cubeRepr[Cube.__BACK][2][0]

        # Take advantage of FRONT-BACK symmetry to reuse the F code. See code for R.
        elif move == Cube.Move.B:
            self.__flipCubeAcrossAxis(Cube.__Axis.UP_DOWN)
            self.turn(Cube.Move.F)
            self.__flipCubeAcrossAxis(Cube.__Axis.UP_DOWN)

        # Take advantage of RIGHT-LEFT symmetry to reuse the R code.
        elif move == Cube.Move.L:
            # Rotate the cube 180 degrees around the UP-DOWN axis.
            self.__flipCubeAcrossAxis(Cube.__Axis.UP_DOWN)
            # Now, do the normal right rotation. This is just one level of recursion.
            self.turn(Cube.Move.R)
            # Undo the flip by flipping again
            self.__flipCubeAcrossAxis(Cube.__Axis.UP_DOWN)


    def draw(self):
        print()

        # Full U face.
        for row in range(3):
            print(13 * " ", end="")
            for col in range(3):
                cell = self.__cubeRepr[Cube.__UP][row][col]
                print(f" {Fore.BLACK}{self.__colorMapping[cell]}{row}{col}", end="")
            print(" ")
        print()

        # First row of L, F, R, B faces
        for row in range(3):
            print("| ", end="")
            for face in [Cube.__LEFT, Cube.__FRONT, Cube.__RIGHT, Cube.__BACK]:
                for col in range(3):
                    cell = self.__cubeRepr[face][row][col]
                    print(f" {Fore.BLACK}{self.__colorMapping[cell]}{row}{col}", end="")
                print(" |", end="")
            print()
        print()

        # Full D face.
        for row in range(3):
            print(13 * " ", end="")
            for col in range(3):
                cell = self.__cubeRepr[Cube.__DOWN][row][col]
                print(f" {Fore.BLACK}{self.__colorMapping[cell]}{row}{col}", end="")
            print(" ")
        print()
        print()

    def __init__(self):
        self.__cubeRepr = [
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



if __name__ == "__main__":
    init(autoreset=True)

    a = Cube()
    a.draw()
    a.turn(Cube.Move.B)
    a.turn(Cube.Move.L)
    a.draw()