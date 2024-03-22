import datetime
import math
import random
from typing import Union, Optional

import click


@click.command()
def main():
    GOSUB_5460()
    PRINT("                          STAR TREK ")
    A = input("DO YOU WANT INSTRUCTIONS (THEY'RE LONG!)")
    if A != "YES":
        _230_program_starts_here()
    else:
        GOSUB_5820()


def PRINT(*args):
    print(*args)


def PRINT_USING(image, *args):
    print(image % args)


def IMAGE(*args): return ''.join(*args)


_X = ' '
_8X = 8 * _X
_3A = '%s'
_6A = '%s'
_D = '%s'
_3D = '%s'
_5D = '%s'


def INT(x):
    return math.ceil(x)


def RND(x):
    return random.random()


global A_, C_, D_, E_, Q_, R_, S_, Z_
global C, D, E, G, I, J, K, N, P, S, T, X, Z
global D0, E0, P0, T0
global Q1, R1, S1, Z1
global Q2, R2, S2, Z2
global B3, K3, S3, Z3
global K7, T7
global H8, S8
global B9, K9, S9, T9


class DIM:
    def __init__(self, d1, d2=0):
        if d2:
            self._ = [DIM(d2) for _ in range(d1)]
        else:
            self._ = [None for _ in range(d1)]

    def __getitem__(self, index: int) -> Union[None, str, int, float, 'DIM']:
        assert 1 <= index <= len(self._)
        return self._[index - 1]

    def __setitem__(self, index: int, value):
        assert 1 <= index <= len(self._)
        self._[index - 1] = value

    def ZER(self):
        for i in range(len(self._)):
            if type(self._[i]) is DIM:
                if self._[i] is not None:
                    self._: Union[str, int, float, 'DIM']
                    self._[i].ZER()
            else:
                self._[i] = 0

    def __repr__(self):
        return '[' + ','.join([str(x) for x in self._]) + ']'


def FND(D):
    math.sqrt((K[I][1] - S1) ** 2 + (K[I][2] - S2) ** 2)


def TIM(x):
    now = datetime.datetime.now()
    if x == 0:
        return now.minute
    if x == 1:
        return now.hour
    assert False


def _230_program_starts_here():
    global Z_
    Z_ = "                                                                      "
    GOSUB_5460()
    global G, C, K, N, Z, C_, D_, E_, A_, Q_, R_, S_, T0, T, T9, D0, E0, E, P0, P, S9, S, H8, Q1, Q2, S1, S2, T7
    G = DIM(8, 8)
    C = DIM(9, 2)
    K = DIM(3, 3)
    N = DIM(3)
    Z = DIM(8, 8)
    C_ = DIM(6)
    D_ = DIM(72)
    E_ = DIM(24)
    A_ = DIM(3)
    Q_ = DIM(72)
    R_ = DIM(72)
    S_ = DIM(48)
    T0 = T = INT(RND(1) * 20 + 20) * 100
    T9 = 30
    D0 = 0
    E0 = E = 3000
    P0 = P = 10
    S9 = 200
    S = H8 = 0
    Q1 = INT(RND(1) * 8 + 1)
    Q2 = INT(RND(1) * 8 + 1)
    S1 = INT(RND(1) * 8 + 1)
    S2 = INT(RND(1) * 8 + 1)
    T7 = TIM(0) + 60 * TIM(1)
    C[2][1] = C[3][1] = C[4][1] = C[4][2] = C[5][2] = C[6][2] = -1
    C[1][1] = C[3][2] = C[5][1] = C[7][2] = C[9][1] = 0
    C[1][2] = C[2][2] = C[6][1] = C[7][1] = C[8][1] = C[8][2] = C[9][2] = 1
    D.ZER()
    D_ = "WARP ENGINESS.R. SENSORSL.R. SENSORSPHASER CNTRLPHOTON TUBESDAMAGE CNTRL"
    E_ = "SHIELD CNTRLCOMPUTER"

    global B9, K9
    B9 = K9 = 0
    while B9 <= 0 or K9 <= 0:
        B9 = K9 = 0
        global I
        for I in range(1, 8 + 1):
            global J
            for J in range(1, 8 + 1):
                global R1
                R1 = RND(1)
                global K3
                if R1 > .98:
                    K3 = 3
                    K9 = K9 + 3
                elif R1 > .95:
                    K3 = 2
                    K9 = K9 + 2
                elif R1 > .8:
                    K3 = 1
                    K9 = K9 + 1
                else:
                    K3 = 0
                R1 = RND(1)
                global B3
                if R1 > .96:
                    B3 = 1
                    B9 = B9 + 1
                else:
                    B3 = 0
                global S3
                S3 = INT(RND(1) * 8 + 1)
                G[I][J] = K3 * 100 + B3 * 10 + S3
                Z[I][J] = 0
        global K7
        K7 = K9
    PRINT("YOU MUST DESTROY", K9, "KLINGONS IN", T9, "STARDATES WITH", B9, "STARBASES")
    K3 = B3 = S3 = 0
    global X
    # 820
    if not (Q1 < 1 or Q1 > 8 or Q2 < 1 or Q2 > 8):  # -> 920
        # 830
        # 870
        if not (K3 == 0):
            # 880
            if not (S > 200):
                # 890
                PRINT("COMBAT AREA      CONDITION RED")
                PRINT("   SHIELDS DANGEROUSLY LOW")
        # 910
        K.ZER()
    # 920
    for I in range(1, 3 + 1):
        K[I][3] = 0
    # 950
    Q_ = Z_
    R_ = Z_
    S_ = Z_[1][48]
    A_ = "<*>"
    global Z1, Z2
    Z1 = S1
    Z2 = S2
    # 1010
    GOSUB_5510()
    # 1020
    for I in range(1, K3 + 1):
        # 1030
        GOSUB_5380()
        # 1040
        A_ = "+++"
        Z1 = R1
        Z2 = R2
        # 1070
        GOSUB_5510()
        # 1080
        K[I][1] = R1
        K[I][2] = R2
        K[I][3] = S9
    # 1120
    for I in range(1, B3 + 1):
        # 1130
        GOSUB_5380()
        # 1140
        A_ = ">!<"
        Z1 = R1
        Z2 = R2
        # 1170
        GOSUB_5510()
    # 1190
    for I in range(1, S3 + 1):
        # 1200
        GOSUB_5380()
        # 1210
        A_ = " * "
        Z1 = R1
        Z2 = R2
        # 1240
        GOSUB_5510()
    # 1260
    GOSUB_4120()
    # 1270
    ...


# regular end of loop in 4210
# 4220  D0=0
# 4230  GOTO 4310

# after loop break in 4190
# 4240  D0=1
# 4250  C$="DOCKED"
# 4260  E=3000
# 4270  P=10
# 4280  PRINT "SHIELDS DROPPED FOR DOCKING PURPOSES"
# 4290  S=0
# 4300  GOTO 4380

# rest of regular end of loop from 4230
# 4310  IF K3>0 THEN 4350
# 4320  IF E<E0*.1 THEN 4370
# 4330  C$="GREEN"
# 4340  GOTO 4380

# 4350  C$="RED"
# 4360  GOTO 4380

# 4370  C$="YELLOW"

# from 4370, 4360 4340 4300
# 4380  IF D[2] >= 0 THEN 4430

# from 4380
# 4390  PRINT
# 4400  PRINT "*** SHORT RANGE SENSORS ARE OUT ***"
# 4410  PRINT
# 4420  GOTO 4530

# from 4380
# 4430  PRINT  USING 4540
# 4440  PRINT  USING 4550;Q$[1,3],Q$[4,6],Q$[7,9],Q$[10,12],Q$[13,15],Q$[16,18],Q$[19,21],Q$[22,24]
# 4450  PRINT  USING 4560;Q$[25,27],Q$[28,30],Q$[31,33],Q$[34,36],Q$[37,39],Q$[40,42],Q$[43,45],Q$[46,48],T
# 4460  PRINT  USING 4570;Q$[49,51],Q$[52,54],Q$[55,57],Q$[58,60],Q$[61,63],Q$[64,66],Q$[67,69],Q$[70,72],C$
# 4470  PRINT  USING 4580;R$[1,3],R$[4,6],R$[7,9],R$[10,12],R$[13,15],R$[16,18],R$[19,21],R$[22,24],Q1,Q2
# 4480  PRINT  USING 4590;R$[25,27],R$[28,30],R$[31,33],R$[34,36],R$[37,39],R$[40,42],R$[43,45],R$[46,48],S1,S2
# 4490  PRINT  USING 4600;R$[49,51],R$[52,54],R$[55,57],R$[58,60],R$[61,63],R$[64,66],R$[67,69],R$[70,72],E
# 4500  PRINT  USING 4610;S$[1,3],S$[4,6],S$[7,9],S$[10,12],S$[13,15],S$[16,18],S$[19,21],S$[22,24],P
# 4510  PRINT  USING 4620;S$[25,27],S$[28,30],S$[31,33],S$[34,36],S$[37,39],S$[40,42],S$[43,45],S$[46,48],S
# 4520  PRINT  USING 4540

# from 4520, 4420
# 4530  RETURN


def GOSUB_4120():
    global I
    # 4120
    for I in range(S1 - 1, S1 + 1 + 1):
        global J
        # 4130
        for J in range(S2 - 1, S2 + 1 + 1):
            # 4140
            if not (I < 1 or I > 8 or J < 1 or J > 8):  # otherwise 4200
                # 4150
                global A_, Z1, Z2
                A_ = ">!<"
                Z1 = I
                Z2 = J
                # 4180
                GOSUB_5680()
                # 4190
                if Z3 == 1:  # else 4200
                    # 4240
                    global D0, C_, E, P, S
                    D0 = 1
                    C_ = "DOCKED"
                    E = 3000
                    P = 10
                    PRINT("SHIELDS DROPPED FOR DOCKING PURPOSES")
                    S = 0
                    # 4300 GOTO 4380
    # 4200
    # 4220
    D0 = 0
    # 4230 GOTO 4310
    # 4310
    ...
    # 4380
    if D[2] >= 0:
        # 4430
        PRINT_USING(_4540)
        PRINT_USING(_4550, Q_[1][3],Q_[4][6],Q_[7][9],Q_[10][12],Q_[13][15],Q_[16][18],Q_[19][21],Q_[22][24])
    else:
        # 4390
        PRINT()
        PRINT("*** SHORT RANGE SENSORS ARE OUT ***")
        PRINT()
        # 4420 GOTO 4530
    # 4530 RETURN


_4540 = IMAGE("---------------------------------")
_4550 = IMAGE(8 * (_X + _3A))
_4560 = IMAGE(8 * (_X + _3A), _8X, "STARDATE", _8X, _5D)
_4570 = IMAGE(8 * (_X + _3A), _8X, "CONDITION", _8X, _6A)
_4580 = IMAGE(8 * (_X + _3A), _8X, "QUADRANT", 9 * _X, _D, ",", _D)
_4590 = IMAGE(8 * (_X + _3A), _8X, "SECTOR", 11 * _X, _D, ",", _D)
_4600 = IMAGE(8 * (_X + _3A), _8X, "ENERGY", 9 * _X, 6 * _D)
_4610 = IMAGE(8 * (_X + _3A), _8X, "PHOTON TORPEDOES", _3D)
_4620 = IMAGE(8 * (_X + _3A), _8X, "SHIELDS", _8X, *_D)


def GOSUB_5380():
    global Z3
    Z3 = 0
    while Z3 == 0:
        global R1, R2, A_, Z1, Z2
        R1 = INT(RND(1) * 8 + 1)
        R2 = INT(RND(1) * 8 + 1)
        A_ = "   "
        Z1 = R1
        Z2 = R2
        GOSUB_5680()


def GOSUB_5680():
    global Z1, Z2, S8, Z3
    # *******  STRING COMPARISON IN QUADRANT ARRAY **********
    Z1 = INT(Z1 + .5)
    Z2 = INT(Z2 + .5)
    S8 = Z1 * 24 + Z2 * 3 - 26
    Z3 = 0
    if not (S8 > 72):
        if Q_[S8][S8 + 2] != A_:
            return
        else:
            Z3 = 1
            return
    if not (S8 > 144):
        if R_[S8 - 72][S8 - 70] != A_:
            return
    else:
        Z3 = 1
        return


def GOSUB_5510():
    global S8
    # ******  INSERTION IN STRING ARRAY FOR QUADRANT ******
    S8 = Z1 * 24 + Z2 * 3 - 26
    if not (S8 > 72):
        Q_[S8][S8 + 2] = A_
        return
    if not (S8 > 144):
        R_[S8 - 72][S8 - 70] = A_
        return
    S_[S8 - 144][S8 - 142] = A_
    return


def GOSUB_5820():
    PRINT("     INSTRUCTIONS:")
    PRINT("<*> = ENTERPRISE")
    PRINT("+++ = KLINGON")
    PRINT(">!< = STARBASE")
    PRINT(" *  = STAR")
    PRINT("COMMAND 0 = WARP ENGINE CONTROL")
    PRINT("  'COURSE' IS IN A CIRCULAR NUMERICAL          4  3  2")
    PRINT("  VECTOR ARRANGEMENT AS SHOWN.                  \\ ^ /")
    PRINT("  INTEGER AND REAL VALUES MAY BE                 \\^/")
    PRINT("  USED.  THEREFORE COURSE 1.5 IS              5 ----- 1")
    PRINT("  HALF WAY BETWEEN 1 AND 2.                      /^\\")
    PRINT("                                                / ^ \\")
    PRINT("  A VECTOR OF 9 IS UNDEFINED, BUT              6  7  8")
    PRINT("  VALUES MAY APPROACH 9.")
    PRINT("                                               COURSE")
    PRINT("  ONE 'WARP FACTOR' IS THE SIZE OF")
    PRINT("  ONE QUADRANT.  THEREFORE TO GET")
    PRINT("  FROM QUADRANT 6,5 TO 5,5 YOU WOULD")
    PRINT("  USE COURSE 3, WARP FACTOR 1")
    PRINT("COMMAND 1 = SHORT RANGE SENSOR SCAN")
    PRINT("  PRINTS THE QUADRANT YOU ARE CURRENTLY IN, INCLUDING")
    PRINT("  STARS, KLINGONS, STARBASES, AND THE ENTERPRISE; ALONG")
    PRINT("  WITH OTHER PERTINATE INFORMATION.")
    PRINT("COMMAND 2 = LONG RANGE SENSOR SCAN")
    PRINT("  SHOWS CONDITIONS IN SPACE FOR ONE QUADRANT ON EACH SIDE")
    PRINT("  OF THE ENTERPRISE IN THE MIDDLE OF THE SCAN.  THE SCAN")
    PRINT("  IS CODED IN THE FORM XXX, WHERE THE UNITS DIGIT IS THE")
    PRINT("  NUMBER OF STARS, THE TENS DIGIT IS THE NUMBER OF STAR-")
    PRINT("  BASES, THE HUNDREDS DIGIT IS THE NUMBER OF KLINGONS.")
    PRINT("COMMAND 3 = PHASER CONTROL")
    PRINT("  ALLOWS YOU TO DESTROY THE KLINGONS BY HITTING HIM WITH")
    PRINT("  SUITABLY LARGE NUMBERS OF ENERGY UNITS TO DEPLETE HIS ")
    PRINT("  SHIELD POWER.  KEEP IN MIND THAT WHEN YOU SHOOT AT")
    PRINT("  HIM, HE GONNA DO IT TO YOU TOO.")
    PRINT("COMMAND 4 = PHOTON TORPEDO CONTROL")
    PRINT("  COURSE IS THE SAME AS USED IN WARP ENGINE CONTROL")
    PRINT("  IF YOU HIT THE KLINGON, HE IS DESTROYED AND CANNOT FIRE")
    PRINT("  BACK AT YOU.  IF YOU MISS, HE WILL SHOOT HIS PHASERS AT")
    PRINT("  YOU.")
    PRINT("   NOTE: THE LIBRARY COMPUTER (COMMAND 7) HAS AN OPTION")
    PRINT("   TO COMPUTE TORPEDO TRAJECTORY FOR YOU (OPTION 2).")
    PRINT("COMMAND 5 = SHIELD CONTROL")
    PRINT("  DEFINES NUMBER OF ENERGY UNITS TO BE ASSIGNED TO SHIELDS")
    PRINT("  ENERGY IS TAKEN FROM TOTAL SHIP'S ENERGY.")
    PRINT("COMMAND 6 = DAMAGE CONTROL REPORT")
    PRINT("  GIVES STATE OF REPAIRS OF ALL DEVICES.  A STATE OF REPAIR")
    PRINT("  LESS THAN ZERO SHOWS THAT THAT DEVICE IS TEMPORARALY")
    PRINT("  DAMAGED.")
    PRINT("COMMAND 7 = LIBRARY COMPUTER")
    PRINT("  THE LIBRARY COMPUTER CONTAINS THREE OPTIONS:")
    PRINT("    OPTION 0 = CUMULATIVE GALACTIC RECORD")
    PRINT("     SHOWS COMPUTER MEMORY OF THE RESULTS OF ALL PREVIOUS")
    PRINT("     LONG RANGE SENSOR SCANS")
    PRINT("    OPTION 1 = STATUS REPORT")
    PRINT("     SHOWS NUMBER OF KLINGONS, STARDATES AND STARBASES")
    PRINT("     LEFT.")
    PRINT("    OPTION 2 = PHOTON TORPEDO DATA")
    PRINT("     GIVES TRAJECTORY AND DISTANCE BETWEEN THE ENTERPRISE")
    PRINT("     AND ALL KLINGONS IN YOUR QUADRANT")


def GOSUB_5460():
    i = 1
    while i <= 11:
        PRINT()
        i += 1


if __name__ == '__main__':
    main()
