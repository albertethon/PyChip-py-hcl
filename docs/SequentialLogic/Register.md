---
sort: 1
---

# Registers
## Introduction
Register is the basic elements in the circuit. Register is state elements, and it is the most important part in sequential circuit.
## Instantiation
 We provide two APIs to define a register:

|        Syntax        |                          Description                           |
|:--------------------:|:--------------------------------------------------------------:|
|   Reg(<cdatatype>)   |           Register definition without initial value            |
| RegInit(<cdatatype>) | Register loaded with the given resetValue when a reset occurs  |

We give a example of using register:

```python
count = RegInit(U.w(16)(0))
count <<= count + U(1)
```

## Reset Value

`RegInit(<cdatatype>)` directly creates the register with a reset value.

## Initialization value for simulation purpose
## Register values
## Transforming wire into a register