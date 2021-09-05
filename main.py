from colorama import Back, init, Style, Fore

def printCube(cube):
    t = {
        'r': Back.RED,
        'g': Back.GREEN,
        'o': Back.MAGENTA, # No orange :(
        'b': Back.BLUE,
        'y': Back.YELLOW,
        'w': Back.WHITE,
    }

    # Top Padding
    print('\n' * 2)

    # Full U face.
    for row in cube[4]:
        print(13 * " ", end="")
        for cell in row:
            print(f" {t[cell]}  ", end="")
        print(" ")

    # First row of L, F, R, B faces
    for row in [0, 1, 2]:
        print("| ", end="")
        for face in [3, 0, 1, 2]:
            for cell in cube[face][row]:
                print(f" {t[cell]}  ", end="")
            print(" |", end="")
        print()

    # Full D face.
    for row in cube[5]:
        print(13 * " ", end="")
        for cell in row:
            print(f" {t[cell]}  ", end="")
        print(" ")

    # Bottom Padding
    print('\n' * 2)

if __name__ == "__main__":
    init(autoreset=True)

    cube = [
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

    printCube(cube)