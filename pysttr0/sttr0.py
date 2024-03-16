import datetime
import math
import random

import click


@click.command()
def main():
    gosub_5460()
    print("                          STAR TREK ")
    A = input("DO YOU WANT INSTRUCTIONS (THEY'RE LONG!)")
    if A != "YES":
        _230_program_starts_here()
    else:
        gosub_5820()


def INT(x):
    return math.ceil(x)


def RND(x):
    return random.random()


global S1
global I


class DIM:
    def __init__(self, d1, d2=0):
        if d2:
            self._ = [DIM(d2) for _ in range(d1)]
        else:
            self._ = [None for _ in range(d1)]

    def __getitem__(self, index):
        assert 1 <= index <= len(self._)
        return self._[index - 1]

    def __setitem__(self, index, value):
        assert 1 <= index <= len(self._)
        self._[index - 1] = value

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
    global Z_, G, C, K, N, Z, C_, D_, E_, A_, Q_, R_, S_, T0, T
    global T9, D0, E0, E, P0, P, S9, S, H8, Q1, Q2, S1, S2, T7
    global B9, K9, I, J, R1, K3, B3, S3, K7
    Z_ = "                                                                      "
    gosub_5460()
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
    # MAT D=ZER
    D_ = "WARP ENGINESS.R. SENSORSL.R. SENSORSPHASER CNTRLPHOTON TUBESDAMAGE CNTRL"
    E_ = "SHIELD CNTRLCOMPUTER"

    B9 = K9 = 0
    while B9 <= 0 or K9 <= 0:
        B9 = K9 = 0
        for I in range(1, 8 + 1):
            for J in range(1, 8 + 1):
                R1 = RND(1)
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
                if R1 > .96:
                    B3 = 1
                    B9 = B9 + 1
                else:
                    B3 = 0
                S3 = INT(RND(1) * 8 + 1)
                G[I][J] = K3 * 100 + B3 * 10 + S3
                Z[I][J] = 0
        K7 = K9
    print("YOU MUST DESTROY", K9, "KLINGONS IN", T9, "STARDATES WITH", B9, "STARBASES")


def gosub_5820():
    print("     INSTRUCTIONS:")
    print("<*> = ENTERPRISE")
    print("+++ = KLINGON")
    print(">!< = STARBASE")
    print(" *  = STAR")
    print("COMMAND 0 = WARP ENGINE CONTROL")
    print("  'COURSE' IS IN A CIRCULAR NUMERICAL          4  3  2")
    print("  VECTOR ARRANGEMENT AS SHOWN.                  \\ ^ /")
    print("  INTEGER AND REAL VALUES MAY BE                 \\^/")
    print("  USED.  THEREFORE COURSE 1.5 IS              5 ----- 1")
    print("  HALF WAY BETWEEN 1 AND 2.                      /^\\")
    print("                                                / ^ \\")
    print("  A VECTOR OF 9 IS UNDEFINED, BUT              6  7  8")
    print("  VALUES MAY APPROACH 9.")
    print("                                               COURSE")
    print("  ONE 'WARP FACTOR' IS THE SIZE OF")
    print("  ONE QUADRANT.  THEREFORE TO GET")
    print("  FROM QUADRANT 6,5 TO 5,5 YOU WOULD")
    print("  USE COURSE 3, WARP FACTOR 1")
    print("COMMAND 1 = SHORT RANGE SENSOR SCAN")
    print("  PRINTS THE QUADRANT YOU ARE CURRENTLY IN, INCLUDING")
    print("  STARS, KLINGONS, STARBASES, AND THE ENTERPRISE; ALONG")
    print("  WITH OTHER PERTINATE INFORMATION.")
    print("COMMAND 2 = LONG RANGE SENSOR SCAN")
    print("  SHOWS CONDITIONS IN SPACE FOR ONE QUADRANT ON EACH SIDE")
    print("  OF THE ENTERPRISE IN THE MIDDLE OF THE SCAN.  THE SCAN")
    print("  IS CODED IN THE FORM XXX, WHERE THE UNITS DIGIT IS THE")
    print("  NUMBER OF STARS, THE TENS DIGIT IS THE NUMBER OF STAR-")
    print("  BASES, THE HUNDREDS DIGIT IS THE NUMBER OF KLINGONS.")
    print("COMMAND 3 = PHASER CONTROL")
    print("  ALLOWS YOU TO DESTROY THE KLINGONS BY HITTING HIM WITH")
    print("  SUITABLY LARGE NUMBERS OF ENERGY UNITS TO DEPLETE HIS ")
    print("  SHIELD POWER.  KEEP IN MIND THAT WHEN YOU SHOOT AT")
    print("  HIM, HE GONNA DO IT TO YOU TOO.")
    print("COMMAND 4 = PHOTON TORPEDO CONTROL")
    print("  COURSE IS THE SAME AS USED IN WARP ENGINE CONTROL")
    print("  IF YOU HIT THE KLINGON, HE IS DESTROYED AND CANNOT FIRE")
    print("  BACK AT YOU.  IF YOU MISS, HE WILL SHOOT HIS PHASERS AT")
    print("  YOU.")
    print("   NOTE: THE LIBRARY COMPUTER (COMMAND 7) HAS AN OPTION")
    print("   TO COMPUTE TORPEDO TRAJECTORY FOR YOU (OPTION 2).")
    print("COMMAND 5 = SHIELD CONTROL")
    print("  DEFINES NUMBER OF ENERGY UNITS TO BE ASSIGNED TO SHIELDS")
    print("  ENERGY IS TAKEN FROM TOTAL SHIP'S ENERGY.")
    print("COMMAND 6 = DAMAGE CONTROL REPORT")
    print("  GIVES STATE OF REPAIRS OF ALL DEVICES.  A STATE OF REPAIR")
    print("  LESS THAN ZERO SHOWS THAT THAT DEVICE IS TEMPORARALY")
    print("  DAMAGED.")
    print("COMMAND 7 = LIBRARY COMPUTER")
    print("  THE LIBRARY COMPUTER CONTAINS THREE OPTIONS:")
    print("    OPTION 0 = CUMULATIVE GALACTIC RECORD")
    print("     SHOWS COMPUTER MEMORY OF THE RESULTS OF ALL PREVIOUS")
    print("     LONG RANGE SENSOR SCANS")
    print("    OPTION 1 = STATUS REPORT")
    print("     SHOWS NUMBER OF KLINGONS, STARDATES AND STARBASES")
    print("     LEFT.")
    print("    OPTION 2 = PHOTON TORPEDO DATA")
    print("     GIVES TRAJECTORY AND DISTANCE BETWEEN THE ENTERPRISE")
    print("     AND ALL KLINGONS IN YOUR QUADRANT")


def gosub_5460():
    i = 1
    while i <= 11:
        print()
        i += 1


if __name__ == '__main__':
    main()
