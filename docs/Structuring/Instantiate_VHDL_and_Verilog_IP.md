---
sort: 5
---

# Instantiate Verilog IP
## Description
A blackbox allows the user to integrate an existing Verilog component into the design by just specifying its interfaces. It’s up to the simulator or synthesizer to do the elaboration correctly.

## Defining an black box
An example of how to define a blackbox is shown below:
```python
class BBox(BlackBox):
    io = IO(
        in1=Input(U.w(64)),
        in2=Input(U.w(64)),
        out=Output(U.w(64)),
    )
```
## Generics
## Instantiating a blackbox

```python
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
    bbox.io.in1 @= io.i
    bbox.io.in2 @= io.i
    io.o @= bbox.io.out

if __name__ == '__main__':
    Emitter.dump(Emitter.emit(M(), Verilog), "M.v")
```

## Clock and reset mapping
## io prefix
## Rename all io of a blackbox
## Add RTL source
## VHDL No numeric type