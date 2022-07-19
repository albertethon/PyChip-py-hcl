# Getting Started

SpinalHDL is a hardware description language written in Scala, a statically-typed functional language using the Java virtual machine (JVM). In order to start programming with SpinalHDL, you must have a JVM as well as the Scala compiler. In the next section, we will explain how to download those tools if you don’t have them already.


## Requirements / Things to download to get started

Before you download the SpinalHDL tools, you need to install:
* Python 3.7 or above
* FIRRTL environment

### FIRRTL
Firrtl is an intermediate representation (IR) for digital circuits designed as a platform for writing circuit-level transformations. In Chisel3 version, the framework tools are compiled in a chain from Scala to FIRRTL to Verilog. the introduction of FIRRTL makes the front and back end of the framework practically replaceable with other languages. the target language of PyHCL is FIRRTL and calls the FIRRTL compiler to generate Verilog code. So to use PyHCL you need to configure the FIRRTL environment.
The FIRRTL installation and configuration process is described in detail in the FIRRTL Github repo:

<https://github.com/chipsalliance/firrtl#installation-instructions>

You need to follow the instructions above to install verilator, yosys and sbt, which are the environments that FIRRTL depends on. Then you need to compile and install FIRRTL, and if there are no problems, the FIRRTL executable will be generated in `/firrtl/utils/bin`. Next you need to add it to the system environment variables, for different operating systems, the method of adding environment variables are different, you need to check the method yourself on the Internet. Eventually, if you successfully add firrtl to the environment variables, typing `firrtl --help` in the terminal will display the information about the firrtl command.

## Other tools

## How to start programming with SpinalHDL
### The SBT way
### The IDE way, with IntelliJ IDEA and its Scala plugin
## A very simple SpinalHDL example
### Generated code



```shell
git clone git@github.com:scutdig/PyChip-py-hcl.git
```

## firrtl
https://github.com/chipsalliance/firrtl

## Motivation

With the rapid development of heterogeneous systems, the traditional hardware development methods require innovations. On the one hand, agile hardware development becomes more critical in developing system-on-chips (SoCs) due to its short development cycles and fast prototyping fea-tures. On the other hand, traditional hardware description languages (HDLs) lack productivity and efﬁciency to develop heterogeneous systems. Moreover, there is a significant methodology gap between the current main-stream hardware design and verification tools. In this paper, we introduce PyChip, a novel Python-based full-stack hardware development framework. PyChip includes PyHCL for circuit construction and PyUVM for design verification. To achieve agile hardware development, PyHCL provides a clean and precise interface for developers to rapidly design hardware cir-cuits. PyUVM provides three verification approaches for various verifica-tion levels and strategies, including the capabilities for universal verifica-tion methodology (UVM). Besides, we built a multi-level verification envi-ronment based on the UVM feature provided by PyUVM, which supports the gray-box verification strategy and remains outstanding simulation per-formance and high reusability. The implementation and simulation results show that PyChip has excellent hardware development efficiency and per-formance. The PyHCL implementations have a 69% code density reduction compare to the hand-written Verilog code on average. The two combina-tional verification approaches provided by the multi-level verification en-vironment have 63% and 40% improvement of simulation performance compared to the single approaches, respectively.

## Python Guide
https://www.python.org/about/gettingstarted/










