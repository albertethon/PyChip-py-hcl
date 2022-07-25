---
sort: 1
---

# Assignments
## Assignments
There are multiple assignment operators:

|  Symbol  |                                                            Description                                                                                              |
|:--------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|    =     | Standard assignment, equivalent to <= in Verilog. <br/>The last assignment to a variable wins; <br/>the value is not updated until the next simulation delta cycle. |
| \<\<=,@= |               Automatic connection between 2 signals or two bundles of the same type. <br/>Direction is inferred by using signal direction (in/out).                |

```python
# io.sum <<= a_xor_b ^ io.cin
io.sum @= a_xor_b ^ io.cin
```
## Width checking
## Combinatorial loops