---
sort: 3
---

# Wire
## Introduction
Wire is the a circuit element act as wire in Verilog, for constructing a hardware wire. It preforms a wire connection for other elements operations. Wire cannot store any statement, users could treat it as a node in circuit or in FIRRTL syntax tree. We could define a Wire like this:

```python
w = Wire(<cdatatype>)
```

For example, we want to define a Wire as the node of the addition operation of two circuit elements:

```python
w <<= io.a + io.cin
io.b <<= w	# Connect w to output port b
```

Under certian circumstances, we could implement the same circuit logic without using Wire:

```python
w = io.a + io.cin
io.b <<= w	# The same as the example above
```