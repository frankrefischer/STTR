import datetime
import math
import random
from typing import Union, Optional

import click


@click.command()
def main():
    GOSUB_5460()
    PRINT("                          STAR TREK ")
    global A_
    A_ = INPUT_STR("DO YOU WANT INSTRUCTIONS (THEY'RE LONG!)")
    if A_ != "YES":
        while True:
            try:
                _230_program_starts_here()
            except EnterpriseDestroyed:
                ...
            except EnterpriseDeadInSpace:
                ...
            except TimeOver:
                ...

    else:
        GOSUB_5820()


def PRINT(*args):
    print(*args)


def PRINT_USING(image, *args):
    print(image % args)


def IMAGE(*args): return ''.join(args)


def INPUT_STR(*args):
    return input(*args)


def INPUT_NUM(*args):
    s: str = input(*args)
    if s.isnumeric():
        return float(s)
    else:
        return None


_X = ' '
_8X = 8 * _X
_9X = 9 * _X
_11X = 11 * _X
_3A = '%3s'
_6A = '%6s'
_D = '%1s'
_3D = '%3s'
_4D = '%4s'
_5D = '%5s'
_6D = '%6s'


def INT(x):
    return math.ceil(x)


def RND(x):
    return random.random()


global A_, C_, D_, E_, Q_, R_, S_, Z_
global C, D, E, G, I, J, K, N, P, S, T, X, Z
global D0, E0, P0, T0
global C1, Q1, R1, S1, W1, Z1
global Q2, R2, S2, Z2
global B3, K3, S3, Z3
global K7, T7
global H8, S8
global B9, K9, S9, T9


def DIM_STRING(d: int):
    return STRING(capacity=d)


class STRING:
    def __init__(self, string: Optional[str] = '', capacity: Optional[int] = None):
        assert capacity is None or len(string) == 0 or len(string) == capacity, f'{string=} {capacity=}'
        self.string: str = string
        self.capacity: int = len(string) if capacity is None else capacity
        assert len(self.string) == 0 or len(string) == self.capacity, f'{self.string=} {self.capacity=}'

    def __len__(self):
        return self.capacity

    def __eq__(self, other):
        return other == self.string

    def __getitem__(self, i):
        if isinstance(i, slice):
            i: slice
            return self.string[i.start-1:i.stop]
        else:
            return self.string[i]

    def set(self, string: str):
        assert len(string) == self.capacity

class DIM:
    def __init__(self, d1, d2=0):
        if d2:
            self._ = [DIM(d2) for _ in range(d1)]
        else:
            self._ = [None for _ in range(d1)]

    def __getitem__(self, index: Union[int, slice]) -> Union[None, str, int, float, 'DIM']:
        if type(self._) is str:
            if type(index) is int:
                return self._[index - 1]
            else:
                index: slice
                index_minus_1: slice = DIM._slice_minus_1(index)
                return self._[index_minus_1]
        assert type(index) is int, f'{type(index)=} {index=}'
        assert 1 <= index <= len(self._), f'{index=}'
        return self._[index - 1]

    @staticmethod
    def _slice_minus_1(s: slice) -> slice:
        return slice(
            DIM._optional_int_minus_1(s.start),
            DIM._optional_int_minus_1(s.stop),
            DIM._optional_int_minus_1(s.step),
        )

    @staticmethod
    def _optional_int_minus_1(i: Optional[int]) -> Optional[int]:
        if i is None:
            return None
        else:
            return i - 1

    def __setitem__(self, index: Union[int, slice], value):
        if type(self._) is str:
            return self._.__getitem__(index)
        assert type(index) is int, f'{type(index)=} {index=}'
        assert 1 <= index <= len(self._), f'{index=}'

        assert 1 <= index <= len(self._)
        self._[index - 1] = value

    def __len__(self):
        return self._.__len__()

    def ZER(self):
        for i in range(len(self._)):
            if type(self._[i]) is DIM:
                if self._[i] is not None:
                    self._: Union[str, int, float, 'DIM']
                    self._[i].ZER()
            else:
                self._[i] = 0

    def __repr__(self):
        if type(self._) is str:
            return self._
        else:
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
    Z_ = STRING('                                                                        ')
    Z_ = STRING('........................................................................')
    GOSUB_5460()
    global G, C, D, K, N, Z, C_, D_, E_, A_, Q_, R_, S_, T0, T, T9, D0, E0, E, P0, P, S9, S, H8, Q1, Q2, S1, S2, T7
    G = DIM(8, 8)
    C = DIM(9, 2)
    D = DIM(8)
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
    _810()
    # 1260
    GOSUB_4120()
    while True:
        # 1270
        A = INPUT_NUM("COMMAND:")
        # 1290
        if A == 0:
            _1410_command_0_set_course()
        elif A == 1:
            _1260_command_1_short_range_sensor_scan()
        elif A == 2:
            _2330_command_2_long_range_sensor_scan()
        elif A == 3:
            _2530_command_3_fire_phases()
        elif A == 4:
            _2800_command_4_fire_photon_torpedoes()
        elif A == 5:
            _3460_command_5_shield_control()
        elif A == 6:
            _3560_command_6_damage_control_report()
        elif A == 7:
            _4630_command_7_call_on_libray_computer()
        else:
            _1300_display_commands()


def _810():
    global K3, B3, S3
    # 810
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
    global I
    for I in range(1, 3 + 1):
        K[I][3] = 0
    # 950
    global Q_, R_, S_, A_
    Q_ = Z_
    R_ = Z_
    S_ = Z_[:48]
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


def _1300_display_commands():
    PRINT()
    PRINT("   0 = SET COURSE")
    PRINT("   1 = SHORT RANGE SENSOR SCA")
    PRINT("   2 = LONG RANGE SENSOR SCAN")
    PRINT("   3 = FIRE PHASERS")
    PRINT("   4 = FIRE PHOTON TORPEDOES")
    PRINT("   5 = SHIELD CONTROL")
    PRINT("   6 = DAMAGE CONTROL REPORT")
    PRINT("   7 = CALL ON LIBRARY COMPUTER")
    PRINT()


def _1410_command_0_set_course():
    global C1, W1
    C1 = -1
    W1 = -1
    while C1 < 0 or C1 >= 9 or W1 < 0 or W1 > 8:
        # 1410
        C1 = INPUT_NUM("COURSE (1-9):")
        # 1430
        if C1 == 0:
            return
        # 1450
        W1 = INPUT_NUM("WARP FACTOR (0-8):")
        if not (D[1] >= 0 or W1 <= .2):
            # 1490
            PRINT("WARP ENGINES ARE DAMAGED, MAXIMUM SPEED = WARP .2")
            continue
    # 1510
    if K3 <= 0:
        # 1560
        if E > 0:
            _1610()
        else:
            # 1570
            if S < 1:
                # 3920
                _3920_enterprise_dead_in_space()
            else:
                # 1580
                ...

    else:
        # 1520
        GOSUB_3790()
        # 1530
        if K3 <= 0:
            # 1560
            if E > 0:
                _1610()
            else:
                # 1570
                if S1 < 1:
                    # 3920
                    _3920_enterprise_dead_in_space()
                else:
                    # 1580
                    PRINT("YOU HAVE", E, " UNITS OF ENERGY")
                    PRINT("SUGGEST YOU GET SOME FROM YOUR SHIELDS WHICH HAVE", S, " UNITS LEFT")
                    return
        else:
            # 1540
            if S < 0:
                _4000_enterprise_destroyed()
            else:
                # 1550 GOTO 1610
                ...


def _1610():
    # 1610
    global I, E, T
    for I in range(1, 8 + 1):
        # 1620
        if D[I] >= 0:
            # 1640 NEXT I
            ...
        else:
            # 1630
            D[I] = D[I] + 1
            # 1640 NEXT I
    # 1640 NEXT I
    # 1650
    if RND(1) >= .2:
        # 1810
        ...
    else:
        # 1660
        global R1
        R1 = INT(RND(1) * 8 + 1)
        # 1670
        if RND(1) >= .5:
            # 1750
            D[R1] = D[R1] + (RND(1) * 5 + 1)
            PRINT()
            PRINT("DAMAGE CONTROL REPORT:")
            # 1780
            GOSUB_5610()
            # 1790
            PRINT(" STATE OF REPAIR IMPROVED")
            PRINT()
            global N, W1
            N = INT(W1 * 8)
            global A_, Z1, Z2
            A_ = "   "
            global S1, S2
            Z1 = S1
            Z2 = S2
            # 1850
            GOSUB_5510()
            # 1860
            global X
            X = S1
            Y = S2
            C2 = INT(C1)
            X1 = C[C2][1] + (C[C2 + 1][1] - C[C2][1]) * (C1 - C2)
            X2 = C[C2][2] + (C[C2 + 1][2] - C[C2][2]) * (C1 - C2)
            # 1910
            for I in range(1, N + 1):
                # 1920
                S1 = S1 + X1
                S2 = S2 + X2
                # 1940
                if S1 < .5 or S1 >= 8.5 or S2 < .5 or S2 >= 8.5:
                    # 2170
                    global Q1, Q2
                    X = Q1 * 8 + X + X1 * N
                    Y = Q2 * 8 + Y + X2 * N
                    Q1 = INT(X / 8)
                    Q2 = INT(Y / 8)
                    S1 = INT(X - Q1 * 8 + .5)
                    S2 = INT(Y - Q2 * 8 + .5)
                    # 2230
                    if S1 != 0:
                        # 2260
                        ...
                    else:
                        # 2240
                        Q1 = Q1 - 1
                        S1 = 8
                    # 2260
                    if S2 != 0:
                        # 2290
                        ...
                    else:
                        # 2270
                        Q2 = Q2 - 1
                        S2 = 8
                    # 2290
                    T = T + 1
                    E = E - N + 5
                    # 2310
                    if T > T0 + T9:
                        _3970_time_over()
                    else:
                        # 2320 GOTO 810
                        _810()
                        return
                else:
                    # 1950
                    A_ = STRING('   ')
                    Z1 = S1
                    Z2 = S2
                    # 1980
                    GOSUB_5680()
                    # 1990
                    if Z3 != 0:
                        # 2070 NEXT I
                        ...
                    else:
                        # 2030
                        _5370 = IMAGE(" WARP ENGINES SHUTDOWN AT SECTOR ", D, ",", D, " DUE TO BAD NAVIGATION")
                        PRINT_USING(_5370, S1, S2)
                        S1 = S1 - X1
                        S2 = S2 - X2
                        # 2060 GOTO 2080
                        break
            # 2070 NEXT I
            # 2080
            A_ = STRING('<*>')
            S1 = INT(S1 + .5)
            S2 = INT(S2 + .5)
            Z1 = S1
            Z2 = S2
            # 2110
            GOSUB_5510()
            # 2120
            E = E - N + 5
            # 2130
            if W1 < 1:
                # 2150
                ...
            else:
                # 2140
                T = T + 1
            # 2150
            if T > T0 + T9:
                _3970_time_over()
            else:
                # 2160 GOTO 1260
                ...
        else:
            # 1680
            D[R1] = D[R1] - (RND(1) * 5 + 1)
            PRINT()
            PRINT("DAMAGE CONTROL REPORT:")
            # 1710
            GOSUB_5610()
            PRINT(" DAMAGED")
            PRINT()
            # 1740 GOTO 1810

    # 2160 GOTO 1260
    GOSUB_4120()


def _1260_command_1_short_range_sensor_scan():
    import inspect
    PRINT("NOT YET IMPLEMENTED:", inspect.currentframe().f_code.co_name)


def _2330_command_2_long_range_sensor_scan():
    import inspect
    PRINT("NOT YET IMPLEMENTED:", inspect.currentframe().f_code.co_name)


def _2530_command_3_fire_phases():
    import inspect
    PRINT("NOT YET IMPLEMENTED:", inspect.currentframe().f_code.co_name)


def _2800_command_4_fire_photon_torpedoes():
    import inspect
    PRINT("NOT YET IMPLEMENTED:", inspect.currentframe().f_code.co_name)


def _3460_command_5_shield_control():
    import inspect
    PRINT("NOT YET IMPLEMENTED:", inspect.currentframe().f_code.co_name)


def _3560_command_6_damage_control_report():
    import inspect
    PRINT("NOT YET IMPLEMENTED:", inspect.currentframe().f_code.co_name)


def _4630_command_7_call_on_libray_computer():
    import inspect
    PRINT("NOT YET IMPLEMENTED:", inspect.currentframe().f_code.co_name)


class EnterpriseDeadInSpace(Exception):
    ...


def _3920_enterprise_dead_in_space():
    PRINT("THE ENTERPRISE IS DEAD IN SPACE.  IF YOU SURVIVE ALL IMPENDING")
    PRINT("ATTACK YOU WILL BE DEMOTED TO THE RANK OF PRIVATE")
    # 3940 if IF K3 <= 0 THEN 4020
    while not (K3 <= 0):
        # 3950
        GOSUB_3790()
        # 3960 GOTO 3940
    # 4020
    PRINT("THERE ARE STILL", K9, " KLINGON BATTLE CRUISERS")
    raise EnterpriseDeadInSpace()


class TimeOver(Exception):
    ...


def _3970_time_over():
    PRINT()
    PRINT("IT IS STARDATE", T)
    # 3990 GOTO 4020
    PRINT("THERE ARE STILL", K9, " KLINGON BATTLE CRUISERS")
    raise TimeOver()


def GOSUB_3790():
    # 3790
    if C_ != "DOCKED":
        # 3820
        if K3 <= 0:
            # 3910
            ...
        else:
            # 3830
            global I, S
            for I in range(1, 3 + 1):
                # 3840
                if K[I][3] <= 0:
                    # 3900 NEXT I
                    ...
                else:
                    # 3850
                    H = (K[I][3] / FND(0)) * (2 * RND(1))
                    S = S - H
                    _3880 = IMAGE(_4D, " UNIT HIT ON ENTERPRISE AT SECTOR ", D, ",", D, "   (", _4D, " LEFT)")
                    PRINT_USING(_3880, H, K[I][1], K[I][2], S)
                    # 3890
                    if S < 0:
                        _4000_enterprise_destroyed()
                    else:
                        # 3900 NEXT I
                        ...
            # 3900 NEXT I
        # 3910 RETURN
    else:
        # 3800
        PRINT("STAR BASE SHIELDS PROTECT THE ENTERPRISE")
        # 3810 RETURN


class EnterpriseDestroyed(Exception):
    ...


def _4000_enterprise_destroyed():
    PRINT()
    PRINT("THE ENTERPRISE HAS BEEN DESTROYED.  THE FEDERATION WILL BE CONQUERED")
    PRINT("THERE ARE STILL", K9, " KLINGON BATTLE CRUISERS")
    # 4030 GOTO 230
    raise EnterpriseDestroyed()


def GOSUB_4120():
    global I
    # 4120
    break_flag = False
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
                    # THEN 4240
                    break_flag = True
                    break
        if break_flag:
            break
    global D0, C_, E, P, S
    if not break_flag:
        # 4200
        # 4220
        D0 = 0
        # 4230 GOTO 4310
        # 4310
        if K3 > 0:
            # 4350
            C_ = "RED"
            # 4360 GOTO 4380
        else:
            # 4320
            if E < E0 * .1:
                # THEN 4370
                C_ = "YELLOW"
                # 4380
            else:
                # 4330
                C_ = "GREEN"
                # 4340 GOTO 4380
    if break_flag:
        # 4240
        D0 = 1
        C_ = "DOCKED"
        E = 3000
        P = 10
        PRINT("SHIELDS DROPPED FOR DOCKING PURPOSES")
        S = 0
        # 4300 GOTO 4380
    # 4380
    if D[2] >= 0:
        # 4430
        _4540 = IMAGE("---------------------------------")
        PRINT_USING(_4540)
        PRINT(''.join(' ' * 9 + str(i + 1) for i in range(0, 9)))
        PRINT('1234567890' * 10)
        _4550 = IMAGE(8 * (_X + _3A))
        PRINT_USING(_4550, *(Q_[3 * i:3 * (i + 1)] for i in range(0, 8)))
        _4560 = IMAGE(8 * (_X + _3A), _8X, "STARDATE", _8X, _5D)
        PRINT_USING(_4560, *(Q_[3 * i:3 * (i + 1)] for i in range(8, 16)), T)
        _4570 = IMAGE(8 * (_X + _3A), _8X, "CONDITION", _8X, _6A)
        PRINT_USING(_4570, *(Q_[3 * i:3 * (i + 1)] for i in range(16, 24)), C_)
        _4580 = IMAGE(8 * (_X + _3A), _8X, "QUADRANT", _9X, _D, ",", _D)
        PRINT_USING(_4580, *(R_[3 * i:3 * (i + 1)] for i in range(0, 8)), Q1, Q2)
        _4590 = IMAGE(8 * (_X + _3A), _8X, "SECTOR", _11X, _D, ",", _D)
        PRINT_USING(_4590, *(R_[3 * i:3 * (i + 1)] for i in range(8, 16)), S1, S2)
        _4600 = IMAGE(8 * (_X + _3A), _8X, "ENERGY", _9X, _6D)
        PRINT_USING(_4600, *(R_[3 * i:3 * (i + 1)] for i in range(16, 24)), E)
        _4610 = IMAGE(8 * (_X + _3A), _8X, "PHOTON TORPEDOES", _3D)
        PRINT_USING(_4610, *(S_[3 * i:3 * (i + 1)] for i in range(0, 8)), P)
        _4620 = IMAGE(8 * (_X + _3A), _8X, "SHIELDS", _8X, _6D)
        PRINT_USING(_4620, *(S_[3 * i:3 * (i + 1)] for i in range(8, 16)), S)
        PRINT_USING(_4540)
        # 4530 RETURN
    else:
        # 4390
        PRINT()
        PRINT("*** SHORT RANGE SENSORS ARE OUT ***")
        PRINT()
        # 4420 GOTO 4530
    # 4530 RETURN


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


def GOSUB_5610():
    # ****  PRINTS DEVICE NAME FROM ARRAY *****
    global S8
    S8 = R1 * 12 - 11
    # 5630
    if S8 > 72:
        # 5660
        PRINT(E_[S8 - 72, S8 - 61])
    else:
        # 5640
        PRINT(D_[S8, S8 + 11])
        # 5650 GOTO 5670
    # 5670 RETURN


def GOSUB_5680():
    global Z1, Z2, S8, Z3
    # *******  STRING COMPARISON IN QUADRANT ARRAY **********
    Z1 = INT(Z1 + .5)
    Z2 = INT(Z2 + .5)
    S8 = Z1 * 24 + Z2 * 3 - 26
    Z3 = 0
    if not (S8 > 72):
        if Q_[S8:S8 + 2] != A_:
            return
        else:
            Z3 = 1
            return
    if not (S8 > 144):
        if R_[S8 - 72:S8 - 70] != A_:
            return
    else:
        Z3 = 1
        return


def GOSUB_5510():
    global S8, Q_, R_, S_, A_
    # ******  INSERTION IN STRING ARRAY FOR QUADRANT ******
    S8 = Z1 * 24 + Z2 * 3 - 26
    assert len(Q_) == 72, len(Q_)
    assert len(R_) == 72, len(R_)
    assert len(S_) == 48, len(R_)
    if S8 <= 72:
        Q_[S8] = A_[1]
        Q_[S8 + 1] = A_[2]
        Q_[S8 + 2] = A_[3]
        assert len(Q_) == 72, len(Q_)
    elif S8 <= 144:
        R_[S8 - 72] = A_[1]
        R_[S8 - 72 + 1] = A_[2]
        R_[S8 - 72 + 2] = A_[3]
        assert len(R_) == 72, len(R_)
    else:
        S_[S8 - 144] = A_[1]
        S_[S8 - 144 + 1] = A_[2]
        S_[S8 - 144 + 2] = A_[3]
        assert len(S_) == 48, len(R_)


#                                                              <*>
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
