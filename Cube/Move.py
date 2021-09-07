from enum import Enum

class __Move(Enum):
    # Standard layer rotations.
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
    # Whole cube rotations and flips.
    X = 19
    X_= 20
    X2 = 21
    Y = 22
    Y_= 23
    Y2 = 24
    Z = 25
    Z_= 26
    Z2 = 27

# Aliases to make code more readable.
F = __Move.F
F_ = __Move.F_
F2 = __Move.F2
R = __Move.R
R_ = __Move.R_
R2 = __Move.R2
B = __Move.B
B_ = __Move.B_
B2 = __Move.B2
L = __Move.L
L_ = __Move.L_
L2 = __Move.L2
U = __Move.U
U_ = __Move.U_
U2 = __Move.U2
D = __Move.D
D_ = __Move.D_
D2 = __Move.D2
X = __Move.X
X_ = __Move.X_
X2 = __Move.X2
Y = __Move.Y
Y_ = __Move.Y_
Y2 = __Move.Y2
Z = __Move.Z
Z_ = __Move.Z_
Z2 = __Move.Z2