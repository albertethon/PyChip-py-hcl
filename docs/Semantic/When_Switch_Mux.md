---
sort: 2
---

# When Switch Mux
## When
As in VHDL and Verilog, signals can be conditionally assigned when a specified condition is met:


```python
    with when(cond1):
        r0 @= r0 + U.w(32)(1)
    with elsewhen(cond2):
        r0 @= U.w(32)(0)
    with otherwise():
        r0 @= r0
    io.dout @= r0
```

> you should declare keyword `with` before the condition.

## Switch
### Example
## Local declaration
It is possible to define new signals inside a when/switch statement:

```python
    with when(io.i & io.t):
        tmpa = r0 + U.w(32)(1)
        r0 @= tmpa
    with elsewhen(io.i):
        r0 @= U.w(32)(0)
    with otherwise():
        r0 @= r0
    io.dout @= r0
```

## Mux
If you just need a Mux with a Bool selection signal, there are two equivalent syntaxes:

|            Syntax            | Description                                            |
|:----------------------------:|:-------------------------------------------------------|
| Mux(cond,whenTrue,whenFalse) | Return whenTrue when cond is True, whenFalse otherwise |
|  cond ? whenTrue:whenFalse   | Return whenTrue when cond is True, whenFalse otherwise |

```python
io.o @= Mux(io.i, a, b)
```

## Bitwise selection


