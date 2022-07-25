---
sort: 7
---

# Parametrization
## Introduction

```python
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
```

## Elaboration time parameters
## Optional hardware
