import math
from functools import reduce
from typing import List

from pyhcl import *


def coef(value, by):
    return value * U.w(8)(math.floor(255 * by)) >> 8


r, g, b = Input(U.w(8)), Input(U.w(8)), Input(U.w(8))
gray = coef(r, 0.3) + coef(g, 0.4) + coef(b, 0.3)

class Counter(RawModule):
    io = IO(
        i=Input(Bool),
        t=Input(Bool),
        o=Output(U.w(32)),
    )

    myclk = Clock()
    myrst = Reset()

    with clockdomin(myclk, myrst):
        r0 = RegInit(U.w(32)(0))

    with when(io.i & io.t):
        r0 @= r0 + U.w(32)(1)
    # with elsewhen(io.i):
    #     r0 @= U.w(32)(0)
    # with otherwise():
    #     pass

    io.o @= r0

class FullAdder(Module):
    io = IO(
        i=Input(Bool),
        t=Input(Bool),
        R=Input(U.w(8)),
        G=Input(U.w(8)),
        B=Input(U.w(8)),
        sum=Output(Bool),
        cout=Output(Bool),
        dout=Output(U.w(32)),
    )
    r0 = RegInit(U.w(32)(0))
    r1 = RegInit(U.w(32)(0))
    r2 = RegInit(U.w(32)(0))
    r3 = RegInit(U.w(32)(0))
    testa = U.w(3)(3) + U.w(3)(3)
    r2 = r1 + U(3)
    r3 = r1 + r2
    r1 = U(2)


    with when(io.i & io.t):
        tmpa = r0 + U.w(32)(1)
        r0 @= tmpa
    with elsewhen(io.i):
        r0 @= U.w(32)(0)
    with otherwise():
        r0 @= r0
    io.dout @= testa

class BBox(BlackBox):
    io = IO(
        in1=Input(U.w(64)),
        in2=Input(U.w(64)),
        out=Output(U.w(64)),
    )


class M(Module):
    io = IO(
        i = Input(U.w(64)),
        o = Output(U.w(64)),
    )

    bbox = BBox()
    bbox.io.in1 <<= io.i
    bbox.io.in2 @= io.i
    io.o <<= bbox.io.out

def adder(n: int):
    class Adder(Module):
        io = IO(
            ia=Input(U.w(n)),
            ib=Input(U.w(n)),
            icin=Input(Bool),
            isum=Output(U.w(n)),
            icout=Output(Bool),
        )

        FAs = [FullAdder().io for _ in range(n)]
        carry = Wire(Vec(n + 1, Bool))
        sum = Wire(Vec(n, Bool))

        carry[0] @= io.icin

        io.isum @= CatVecH2L(sum)
        io.icout @= carry[n]

    return Adder()

def myManyDynamicElementVecFir(length: int, consts: List):
    class MyManyDynamicElementVecFir(Module):
        io = IO(
            i=Input(U.w(8)),
            valid=Input(Bool),
            o=Output(U.w(8)),
        )

        taps = [io.i] + [RegInit(U.w(8)(0)) for _ in range(length)]
        for a, b in zip(taps, taps[1:]):
            with when(io.valid):
                b @= a

        m = map(lambda x: x[0] * x[1], zip(taps, consts))
        io.o @= reduce(lambda x, y: x + y, m)

    return MyManyDynamicElementVecFir()

if __name__ == '__main__':
    # emit high firrtl
    # Emitter.dump(Emitter.emit(FullAdder(), HighForm), "FullAdder.fir")
    # emit lowered firrtl
    # Emitter.dump(Emitter.emit(FullAdder(), LowForm), "FullAdder.lo.fir")
    # emit verilog
    Emitter.dump(Emitter.emit(adder(2), Verilog), "adder.v")
