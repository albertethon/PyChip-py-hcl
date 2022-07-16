from pyhcl.tester.executer import TesterExecuter
from pyhcl.ir.low_ir import *
from pyhcl.dsl.emitter import Emitter

class Tester:
    def __init__(self, m: Module):
        circuit = Emitter.elaborate(m)
        self.main = circuit.main
        self.executer = TesterExecuter(circuit)
        self.executer.init_executer()
        
    
    def poke(self, name: str, value: int):
        self.executer.set_value(self.main, name, value)
    
    def peek(self, name: str) -> int:
        res = self.executer.get_value(self.main, name)
        return int(res, 2) if isinstance(res, str) else res
    
    def expect(self, a, b) -> bool:
        return a == b

    def step(self, n):
        self.executer.step(n, self.main)