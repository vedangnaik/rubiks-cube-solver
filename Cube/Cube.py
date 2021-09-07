from colorama import Back, Fore
from enum import Enum
from Cube.Move import *


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

    # Direction enum mainly for self.__rotateFace. Normal = clockwise, Prime = anticlockwise, OneEighty = half-turn.
    class __Direction(Enum):
        Normal = 1
        Prime = 2
        OneEighty = 3

    # Face numbers. An enum is too inconvenient since we only need the numbers.
    FRONT = 0
    RIGHT = 1
    BACK = 2
    LEFT = 3
    UP = 4
    DOWN = 5

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
        if move == F:
            self.__rotateFace(self.cubeRepr[Cube.FRONT], Cube.__Direction.Normal)
            self.cubeRepr[Cube.LEFT][2][2], self.cubeRepr[Cube.UP][2][0], self.cubeRepr[Cube.RIGHT][0][0], self.cubeRepr[Cube.DOWN][0][2] = self.cubeRepr[Cube.DOWN][0][2], self.cubeRepr[Cube.LEFT][2][2], self.cubeRepr[Cube.UP][2][0], self.cubeRepr[Cube.RIGHT][0][0]
            self.cubeRepr[Cube.LEFT][1][2], self.cubeRepr[Cube.UP][2][1], self.cubeRepr[Cube.RIGHT][1][0], self.cubeRepr[Cube.DOWN][0][1] = self.cubeRepr[Cube.DOWN][0][1], self.cubeRepr[Cube.LEFT][1][2], self.cubeRepr[Cube.UP][2][1], self.cubeRepr[Cube.RIGHT][1][0]
            self.cubeRepr[Cube.LEFT][0][2], self.cubeRepr[Cube.UP][2][2], self.cubeRepr[Cube.RIGHT][2][0], self.cubeRepr[Cube.DOWN][0][0] = self.cubeRepr[Cube.DOWN][0][0], self.cubeRepr[Cube.LEFT][0][2], self.cubeRepr[Cube.UP][2][2], self.cubeRepr[Cube.RIGHT][2][0]

        # Take advantage of FRONT-BACK symmetry to reuse the F code. See code for L.
        elif move == B:
            self.turn(Y2)
            self.turn(F)
            self.turn(Y2)

        elif move == R:
            self.__rotateFace(self.cubeRepr[Cube.RIGHT], Cube.__Direction.Normal)
            self.cubeRepr[Cube.FRONT][2][2], self.cubeRepr[Cube.UP][2][2], self.cubeRepr[Cube.BACK][0][0], self.cubeRepr[Cube.DOWN][2][2] = self.cubeRepr[Cube.DOWN][2][2], self.cubeRepr[Cube.FRONT][2][2], self.cubeRepr[Cube.UP][2][2], self.cubeRepr[Cube.BACK][0][0]
            self.cubeRepr[Cube.FRONT][1][2], self.cubeRepr[Cube.UP][1][2], self.cubeRepr[Cube.BACK][1][0], self.cubeRepr[Cube.DOWN][1][2] = self.cubeRepr[Cube.DOWN][1][2], self.cubeRepr[Cube.FRONT][1][2], self.cubeRepr[Cube.UP][1][2], self.cubeRepr[Cube.BACK][1][0]
            self.cubeRepr[Cube.FRONT][0][2], self.cubeRepr[Cube.UP][0][2], self.cubeRepr[Cube.BACK][2][0], self.cubeRepr[Cube.DOWN][0][2] = self.cubeRepr[Cube.DOWN][0][2], self.cubeRepr[Cube.FRONT][0][2], self.cubeRepr[Cube.UP][0][2], self.cubeRepr[Cube.BACK][2][0]

        # Take advantage of RIGHT-LEFT symmetry to reuse the R code.
        elif move == L:
            # Rotate the cube 180 degrees around the UP-DOWN axis.
            self.turn(Y2)
            # Now, do the normal right rotation. This is just one level of recursion.
            self.turn(R)
            # Undo the flip by flipping again
            self.turn(Y2)

        # Since this goes across the rows, we can exploit whole-row swapping to keep this clean.
        elif move == U:
            self.__rotateFace(self.cubeRepr[Cube.UP], Cube.__Direction.Normal)
            self.cubeRepr[Cube.FRONT][0][:], self.cubeRepr[Cube.LEFT][0][:], self.cubeRepr[Cube.BACK][0][:], self.cubeRepr[Cube.RIGHT][0][:] = self.cubeRepr[Cube.RIGHT][0][:], self.cubeRepr[Cube.FRONT][0][:], self.cubeRepr[Cube.LEFT][0][:], self.cubeRepr[Cube.BACK][0][:]
        
        # Take advantage of RIGHT-LEFT symmetry to reuse the U code. See code for L.
        elif move == D:
            self.turn(X2)
            self.turn(U)
            self.turn(X2)

        if move == F_:
            self.__rotateFace(self.cubeRepr[Cube.FRONT], Cube.__Direction.Prime)
            self.cubeRepr[Cube.LEFT][2][2], self.cubeRepr[Cube.UP][2][0], self.cubeRepr[Cube.RIGHT][0][0], self.cubeRepr[Cube.DOWN][0][2] = self.cubeRepr[Cube.UP][2][0], self.cubeRepr[Cube.RIGHT][0][0], self.cubeRepr[Cube.DOWN][0][2], self.cubeRepr[Cube.LEFT][2][2]
            self.cubeRepr[Cube.LEFT][1][2], self.cubeRepr[Cube.UP][2][1], self.cubeRepr[Cube.RIGHT][1][0], self.cubeRepr[Cube.DOWN][0][1] = self.cubeRepr[Cube.UP][2][1], self.cubeRepr[Cube.RIGHT][1][0], self.cubeRepr[Cube.DOWN][0][1], self.cubeRepr[Cube.LEFT][1][2]
            self.cubeRepr[Cube.LEFT][0][2], self.cubeRepr[Cube.UP][2][2], self.cubeRepr[Cube.RIGHT][2][0], self.cubeRepr[Cube.DOWN][0][0] = self.cubeRepr[Cube.UP][2][2], self.cubeRepr[Cube.RIGHT][2][0], self.cubeRepr[Cube.DOWN][0][0], self.cubeRepr[Cube.LEFT][0][2]

        # Take advantage of FRONT-BACK symmetry to reuse the F_ code. See code for L.
        elif move == B_:
            self.turn(Y2)
            self.turn(F_)
            self.turn(Y2)

        elif move == R_:
            self.__rotateFace(self.cubeRepr[Cube.RIGHT], Cube.__Direction.Prime)
            self.cubeRepr[Cube.FRONT][2][2], self.cubeRepr[Cube.UP][2][2], self.cubeRepr[Cube.BACK][0][0], self.cubeRepr[Cube.DOWN][2][2] = self.cubeRepr[Cube.UP][2][2], self.cubeRepr[Cube.BACK][0][0], self.cubeRepr[Cube.DOWN][2][2], self.cubeRepr[Cube.FRONT][2][2]
            self.cubeRepr[Cube.FRONT][1][2], self.cubeRepr[Cube.UP][1][2], self.cubeRepr[Cube.BACK][1][0], self.cubeRepr[Cube.DOWN][1][2] = self.cubeRepr[Cube.UP][1][2], self.cubeRepr[Cube.BACK][1][0], self.cubeRepr[Cube.DOWN][1][2], self.cubeRepr[Cube.FRONT][1][2]
            self.cubeRepr[Cube.FRONT][0][2], self.cubeRepr[Cube.UP][0][2], self.cubeRepr[Cube.BACK][2][0], self.cubeRepr[Cube.DOWN][0][2] = self.cubeRepr[Cube.UP][0][2], self.cubeRepr[Cube.BACK][2][0], self.cubeRepr[Cube.DOWN][0][2], self.cubeRepr[Cube.FRONT][0][2]

        # Take advantage of RIGHT-LEFT symmetry to reuse the R_ code. See code for L.
        elif move == L_:
            self.turn(Y2)
            self.turn(R_)
            self.turn(Y2)

        elif move == U_:
            self.__rotateFace(self.cubeRepr[Cube.UP], Cube.__Direction.Prime)
            self.cubeRepr[Cube.FRONT][0][:], self.cubeRepr[Cube.LEFT][0][:], self.cubeRepr[Cube.BACK][0][:], self.cubeRepr[Cube.RIGHT][0][:] = self.cubeRepr[Cube.LEFT][0][:], self.cubeRepr[Cube.BACK][0][:], self.cubeRepr[Cube.RIGHT][0][:], self.cubeRepr[Cube.FRONT][0][:]
        
        # Take advantage of RIGHT-LEFT symmetry to reuse the U_ code. See code for L.
        elif move == D_:
            self.turn(X2)
            self.turn(U_)
            self.turn(X2)

        # Just do the base move two times.
        elif move == F2:
            self.turn(F)
            self.turn(F)

        elif move == B2:
            self.turn(B)
            self.turn(B)

        elif move == R2:
            self.turn(R)
            self.turn(R)

        elif move == L2:
            self.turn(L)
            self.turn(L)

        elif move == U2:
            self.turn(U)
            self.turn(U)

        elif move == D2:
            self.turn(D)
            self.turn(D)

        elif move == X:
            self.cubeRepr[Cube.FRONT], self.cubeRepr[Cube.UP], self.cubeRepr[Cube.BACK], self.cubeRepr[Cube.DOWN] = self.cubeRepr[Cube.DOWN], self.cubeRepr[Cube.FRONT], self.cubeRepr[Cube.UP], self.cubeRepr[Cube.BACK]
            # BACK and DOWN have inconsistent coordinate systems (like Z), so have to be rotated separately.
            self.__rotateFace(self.cubeRepr[Cube.BACK], Cube.__Direction.OneEighty)
            self.__rotateFace(self.cubeRepr[Cube.DOWN], Cube.__Direction.OneEighty)
            # Standard rotation of RIGHT and LEFT.
            self.__rotateFace(self.cubeRepr[Cube.RIGHT], Cube.__Direction.Normal)
            self.__rotateFace(self.cubeRepr[Cube.LEFT], Cube.__Direction.Prime)

        elif move == X_:
            self.cubeRepr[Cube.FRONT], self.cubeRepr[Cube.UP], self.cubeRepr[Cube.BACK], self.cubeRepr[Cube.DOWN] = self.cubeRepr[Cube.UP], self.cubeRepr[Cube.BACK], self.cubeRepr[Cube.DOWN], self.cubeRepr[Cube.FRONT]
            # BACK and UP also have inconsistent coordinate systems (like Z), so have to be rotated separately.
            self.__rotateFace(self.cubeRepr[Cube.BACK], Cube.__Direction.OneEighty)
            self.__rotateFace(self.cubeRepr[Cube.UP], Cube.__Direction.OneEighty)
            # Standard rotation of RIGHT and LEFT.
            self.__rotateFace(self.cubeRepr[Cube.RIGHT], Cube.__Direction.Prime)
            self.__rotateFace(self.cubeRepr[Cube.LEFT], Cube.__Direction.Normal)

        elif move == X2:
            self.turn(X)
            self.turn(X)

        elif move == Y:
            self.cubeRepr[Cube.FRONT], self.cubeRepr[Cube.RIGHT], self.cubeRepr[Cube.BACK], self.cubeRepr[Cube.LEFT] = self.cubeRepr[Cube.RIGHT], self.cubeRepr[Cube.BACK], self.cubeRepr[Cube.LEFT], self.cubeRepr[Cube.FRONT]
            self.__rotateFace(self.cubeRepr[Cube.UP], Cube.__Direction.Normal)
            self.__rotateFace(self.cubeRepr[Cube.DOWN], Cube.__Direction.Prime)

        elif move == Y_:
            self.cubeRepr[Cube.FRONT], self.cubeRepr[Cube.RIGHT], self.cubeRepr[Cube.BACK], self.cubeRepr[Cube.LEFT] = self.cubeRepr[Cube.LEFT], self.cubeRepr[Cube.FRONT], self.cubeRepr[Cube.RIGHT], self.cubeRepr[Cube.BACK]
            self.__rotateFace(self.cubeRepr[Cube.UP], Cube.__Direction.Prime)
            self.__rotateFace(self.cubeRepr[Cube.DOWN], Cube.__Direction.Normal)

        elif move == Y2:
            self.turn(Y)
            self.turn(Y)
        
        elif move == Z:
            self.cubeRepr[Cube.UP], self.cubeRepr[Cube.RIGHT], self.cubeRepr[Cube.DOWN], self.cubeRepr[Cube.LEFT] = self.cubeRepr[Cube.LEFT], self.cubeRepr[Cube.UP], self.cubeRepr[Cube.RIGHT], self.cubeRepr[Cube.DOWN]
            # All faces need to be rotated since the zeros of UP and DOWN are not in line with those of RIGHT and LEFT
            self.__rotateFace(self.cubeRepr[Cube.UP], Cube.__Direction.Normal)
            self.__rotateFace(self.cubeRepr[Cube.RIGHT], Cube.__Direction.Normal)
            self.__rotateFace(self.cubeRepr[Cube.DOWN], Cube.__Direction.Normal)
            self.__rotateFace(self.cubeRepr[Cube.LEFT], Cube.__Direction.Normal)
            # Standard rotation of front and back.
            self.__rotateFace(self.cubeRepr[Cube.FRONT], Cube.__Direction.Normal)
            self.__rotateFace(self.cubeRepr[Cube.BACK], Cube.__Direction.Prime)

        # See Move Z for the extra rotations.
        elif move == Z_:
            self.cubeRepr[Cube.UP], self.cubeRepr[Cube.RIGHT], self.cubeRepr[Cube.DOWN], self.cubeRepr[Cube.LEFT] = self.cubeRepr[Cube.RIGHT], self.cubeRepr[Cube.DOWN], self.cubeRepr[Cube.LEFT], self.cubeRepr[Cube.UP]
            self.__rotateFace(self.cubeRepr[Cube.UP], Cube.__Direction.Prime)
            self.__rotateFace(self.cubeRepr[Cube.RIGHT], Cube.__Direction.Prime)
            self.__rotateFace(self.cubeRepr[Cube.DOWN], Cube.__Direction.Prime)
            self.__rotateFace(self.cubeRepr[Cube.LEFT], Cube.__Direction.Prime)
            self.__rotateFace(self.cubeRepr[Cube.FRONT], Cube.__Direction.Prime)
            self.__rotateFace(self.cubeRepr[Cube.BACK], Cube.__Direction.Normal)

        elif move == Z2:
            self.turn(Z)
            self.turn(Z)

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

    # Sets up the initial state as the cube being solved, with F = red face, U = yellow face, and D = white face.
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
