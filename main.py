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
        bout=Output(U.w(1)),
    )
    rarray = Reg(Vec(4, U.w(16)))  # A 16-bit 4 length unsigned integer register array

    breg = Reg(Bundle(
        x=U.w(16),
        y=S.w(16),
        z=Bool
    ))
    # io.cout @= Sa.to_uint()
    # breg.x <<= U(12)
    # breg.y <<= S(4)
    # breg.z <<= Bool(False)

if __name__ == '__main__':
    # emit high firrtl
    # Emitter.dumpVerilog(Emitter.dump(Emitter.emit(FullAdder(), HighForm), "FullAdder.fir"))
    # emit lowered firrtl
    # Emitter.dump(Emitter.emit(FullAdder(), LowForm), "FullAdder.lo.fir")
    # emit verilog
    Emitter.dump(Emitter.emit(FullAdder(), Verilog), "FullAdder.v")
