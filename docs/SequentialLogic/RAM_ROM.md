---
sort: 2
---

# RAM/ROM
## Syntax
PyHCL only support combinational/asynchronous-read, sequential/synchronous-write memories using register array. Since that lots of memories of different FPGA manufacturer would provide thier own ip cores for memories. We suggest using the blackbox feature of PyHCL to use memories on devices. 
We could define a memory similar to the Vec datatype:

```python
m = Mem(<size>, <cdatatype>)
```

size is the length of the memory, and cdatatype is the datatype of the memory, only support basic types. The PyHCL built-in memory is a register array:
```python
m = Mem(4, U.w(16))
```
Which would compile to Verilog code:

```python
reg [15:0] m [0:3];
```

To indexing the specific element in memory, we use [] operator to do so. To be noticed, the index must be PyHCL literal unsigned integer:

```python
m[U(0)] <<= U(1)	# Entry 0 becomes unsigned integer value 1
```

## Synchronous enable quirk
## Read-under-write policy
## Mixed-width ram
## Automatic blackboxing
### Blackboxing policy
### Standard memory blackboxes