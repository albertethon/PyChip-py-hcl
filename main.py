from pyhcl import *

class FullAdder(Module):
    io = IO(
        udin=Input(U.w(2)),
        sdin=Input(S.w(2)),
        # b=Input(Bool),
        # cin=Input(Bool),
        # sum=Output(Bool),
        cout=Output(U.w(20)),
        sout=Output(S.w(20)),
        bout=Output(U.w(20)),
    )

    Sa = S(32)
    Sb = S(2)
    Ua = U(31)
    Ub = U(2)
    Uc = ~(Ua & Ub)
    Sc = Sa << 2
    io.cout @= Uc ^ Ub | U(7)
    io.sout @= Sc
    temp = S(5) > S(3)
    io.sout @= temp
if __name__ == '__main__':
    # emit high firrtl
    # Emitter.dump(Emitter.emit(FullAdder(), HighForm), "FullAdder.fir")
    # emit lowered firrtl
    # Emitter.dump(Emitter.emit(FullAdder(), LowForm), "FullAdder.lo.fir")
    # emit verilog
    Emitter.dump(Emitter.emit(FullAdder(), Verilog), "FullAdder.v")
