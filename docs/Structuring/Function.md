---
sort: 3
---

# Function
## Introduction
## RGB to gray
For example, if you want to convert a Red/Green/Blue color into greyscale by using coefficients, you can use functions to apply them:

```python
def coef(value, by):
    return value * U.w(8)(math.floor(255 * by)) >> 8

r, g, b = Input(U.w(8)),Input(U.w(8)),Input(U.w(8))
gray = coef(r, 0.3) + coef(g, 0.4) + coef(b, 0.3)
```

## Valid Ready Payload bus
