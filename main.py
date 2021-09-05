from colorama import Back, init, Style, Fore
from enum import Enum

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

    class __Direction(Enum):
        Normal = 1
        Prime = 2
        OneEighty = 3

    # Face numbers. An enum is too inconvenient.
    __FRONT = 0
    __RIGHT = 1
    __BACK = 2
    __LEFT = 3
    __TOP = 4
    __BOTTOM = 5

    def __rotateFace(self, face, dir):
        if dir == Cube.__Direction.Normal:
            # Rotate corners, then edges. The center is fixed.
            face[0][0], face[0][2], face[2][2], face[2][0] = face[2][0], face[0][0], face[0][2], face[2][2]
            face[1][0], face[0][1], face[1][2], face[2][1] = face[2][1], face[1][0], face[0][1], face[1][2]
        elif dir == Cube.__Direction.Prime:
            pass
        elif dir == Cube.__Direction.OneEighty:
            pass

    def turn(self, move):
        if move == Cube.Move.F:
            self.__rotateFace(self.__cubeRepr[Cube.__FRONT], Cube.__Direction.Normal)
            # Rotate 
            self.__cubeRepr[Cube.__LEFT][2][2], self.__cubeRepr[Cube.__TOP][2][0], self.__cubeRepr[Cube.__RIGHT][0][0], self.__cubeRepr[Cube.__BOTTOM][0][2] = self.__cubeRepr[Cube.__BOTTOM][0][2], self.__cubeRepr[Cube.__LEFT][2][2], self.__cubeRepr[Cube.__TOP][2][0], self.__cubeRepr[Cube.__RIGHT][0][0]
            self.__cubeRepr[Cube.__LEFT][1][2], self.__cubeRepr[Cube.__TOP][2][1], self.__cubeRepr[Cube.__RIGHT][1][0], self.__cubeRepr[Cube.__BOTTOM][0][1] = self.__cubeRepr[Cube.__BOTTOM][0][1], self.__cubeRepr[Cube.__LEFT][1][2], self.__cubeRepr[Cube.__TOP][2][1], self.__cubeRepr[Cube.__RIGHT][1][0]
            self.__cubeRepr[Cube.__LEFT][0][2], self.__cubeRepr[Cube.__TOP][2][2], self.__cubeRepr[Cube.__RIGHT][2][0], self.__cubeRepr[Cube.__BOTTOM][0][0] = self.__cubeRepr[Cube.__BOTTOM][0][0], self.__cubeRepr[Cube.__LEFT][0][2], self.__cubeRepr[Cube.__TOP][2][2], self.__cubeRepr[Cube.__RIGHT][2][0]
        elif move == Cube.Move.R:
            self.__rotateFace(self.__cubeRepr[Cube.__RIGHT], Cube.__Direction.Normal)
            

    def draw(self):
        # Top Padding
        print('\n' * 2)

        # Full U face.
        for row in self.__cubeRepr[4]:
            print(13 * " ", end="")
            for cell in row:
                print(f" {self.__colorMapping[cell]}  ", end="")
            print(" ")
        print()

        # First row of L, F, R, B faces
        for row in [0, 1, 2]:
            print("| ", end="")
            for face in [3, 0, 1, 2]:
                for cell in self.__cubeRepr[face][row]:
                    print(f" {self.__colorMapping[cell]}  ", end="")
                print(" |", end="")
            print()
        print()

        # Full D face.
        for row in self.__cubeRepr[5]:
            print(13 * " ", end="")
            for cell in row:
                print(f" {self.__colorMapping[cell]}  ", end="")
            print(" ")

        # Bottom Padding
        print('\n' * 2)

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
    a.turn(Cube.Move.F)
    a.turn(Cube.Move.R)
    a.draw()