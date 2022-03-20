from typing import List
from pyhcl.ir.low_ir import *
from pyhcl.ir.low_prim import *
from pyhcl.passes._pass import Pass, PassException, Error
from pyhcl.passes.utils import get_width, get_info
from pyhcl.passes.check_types import IllegalResetType, CheckTypes, InvalidConnect

# MaxWidth
maxWidth = 1000000

class UninferredWidth(PassException):
    def __init__(self, info: Info, target: str):
        super().__init__(f'{info}:  Uninferred width for target below. (Did you forget to assign to it?) \n{target}')

class InvalidRange(PassException):
    def __init__(self, info: Info, target: str, i: Type):
        super().__init__(f'{info}: Invalid range {i.serialize()} for target below. (Are the bounds valid?) \n{target}')

class  WidthTooSmall(PassException):
    def __init__(self, info: Info, mname: str, b: int):
        super().__init__(f'{info} : [target {mname}]  Width too small for constant {b}.')

class WidthTooBig(PassException):
    def __init__(self, info: Info, mname: str, b: int):
        super().__init__(f'{info} : [target ${mname}]  Width {b} greater than max allowed width of {maxWidth} bits')       

class DshlTooBig(PassException):
    def __init__(self, info: Info, mname: str):
        super().__init__(f'{info} : [target {mname}]  Width of dshl shift amount must be less than {maxWidth} bits.')

class MultiBitAsClock(PassException):
    def __init__(self, info: Info, mname: str):
        super().__init__(f'{info} : [target {mname}]  Cannot cast a multi-bit signal to a Clock.')

class MultiBitAsAsyncReset(PassException):
    def __init__(self, info: Info, mname: str):
        super().__init__(f'{info} : [target {mname}]  Cannot cast a multi-bit signal to an AsyncReset.')

class NegWidthException(PassException):
    def __init__(self, info: Info, mname: str):
        super().__init__(f'{info}: [target {mname}] Width cannot be negative or zero.')

class BitsWidthException(PassException):
    def __init__(self, info: Info, mname: str, hi: int, width: int, exp: str):
        super().__init__(f'{info}: [target {mname}] High bit {hi} in bits operator is larger than input width {width} in {exp}.')

class HeadWidthException(PassException):
    def __init__(self, info: Info, mname: str, n: int, width: int):
        super().__init__(f'{info}: [target {mname}] Parameter {n} in head operator is larger than input width {width}.')

class TailWidthException(PassException):
    def __init__(self, info: Info, mname: str, n: int, width: int):
        super().__init__(f'{info}: [target {mname}] Parameter {n} in tail operator is larger than input width {width}.')

class CheckWidths(Pass):

    def run(self, c: Circuit):
        errors = Error()

        def gen_target(name: str, subname: str) -> str:
            return f'{name}-{subname}'

        def check_width_w(info: Info, target: str, t: Type, w: Width):
            if type(w) == IntWidth and w.width >= maxWidth:
                errors.append(WidthTooBig(info, target, w.width))
            elif type(w) == IntWidth:
                ...
            else:
                errors.append(UninferredWidth(info, target))
        
        def has_width(typ: Type) -> bool:
            if type(typ) == GroundType and hasattr(typ, 'width') and type(typ.width) == IntWidth:
                return True
            elif type(typ) == GroundType:
                return False
            else:
                raise PassException(f'hasWidth - {typ}')
        
        def check_width_t(info: Info, target: str, t: Type):
            if type(t) == BundleType:
                for f in t.fields:
                    check_width_f(info, target, f)
            else:
                for _, tt in t.__dict__.items():
                    if type(tt) == Type:
                        check_width_t(info, target, tt)
            
            for _, tt in t.__dict__.items():
                if type(tt) == Width:
                    check_width_w(info, target, tt)
        
        def check_width_f(info: Info, target: str, f: Field):
            check_width_t(info, target, f.typ)

        def check_width_e_leaf(info: Info, target: str, expr: Expression):
            if type(expr) == UIntLiteral and get_binary_width(expr.value) > get_width(expr.width):
                errors.append(WidthTooSmall(info, target, expr.value))
            elif type(expr) == SIntLiteral and get_binary_width(expr.value) + 1 > get_width(expr.width):
                errors.append(WidthTooSmall(info, target, expr.value))
            elif type(expr) == DoPrim and len(expr.args) == 2:
                if type(expr.op) == Dshl and has_width(expr.args[0].typ) and get_width(expr.args[1].typ) > maxWidth:
                    errors.append(DshlTooBig(info, target))
            elif type(expr) == DoPrim and len(expr.args) == 1:
                if type(expr.op) == Bits and has_width(expr.args[0].typ) and get_width(expr.args[0].typ) <= expr.consts[0]:
                    errors.append(BitsWidthException(info, target, expr.consts[0], get_width(expr.args[0].typ), expr.serialize()))
                elif type(expr.op) == Head and has_width(expr.args[0].typ) and get_width(expr.args[0].typ) <= expr.args[0]:
                    errors.append(HeadWidthException(info, target, expr.consts[0], get_width(expr.args[0].typ)))
                elif type(expr.op) == Tail and has_width(expr.args[0].typ) and get_width(expr.args[0].typ) <= expr.args[0]:
                    errors.append(TailWidthException(info, target, expr.consts[0], get_width(expr.args[0].typ)))
                elif type(expr.op) == AsClock and get_width(expr.consts[0].typ) != 1:
                    errors.append(MultiBitAsClock(info, target))
        
        def check_width_e(info: Info, target: str, rec_depth: int, e: Expression):
            check_width_e_leaf(info, target, e)
            if type(e) in [Mux, ValidIf, DoPrim]:
                if rec_depth > 0:
                    for _, ee in e.__dict__.items():
                        if type(ee) == Expression:
                            check_width_e(info, target, rec_depth - 1, ee)
                else:
                    check_width_e_dfs(info, target, e)
        
        def check_width_e_dfs(info: Info, target: str, expr: Expression):
            stack = expr.__dict__.items()
            def push(e: Expression):
                stack.append(e)
            while len(stack) > 0:
                current = stack
                check_width_e_leaf(info, target, current)
                for _, leaf in current.__dict__.items():
                    if type(leaf) == Expression:
                        push(leaf)
            
        
        def check_width_s(minfo: Info, target: str, s: Statement):
            info = get_info(s)
            for _, ss in s.__dict__.items():
                if type(ss) == Expression:
                    check_width_e(info, target, 4, ss)
                if type(ss) == Statement:
                    check_width_s(info, target, ss)
                if type(ss) == Type:
                    check_width_t(info, target, ss)
                
            if type(s) == DefRegister:
                sx = s.reset.typ
                if type(sx) == UIntType and get_width(sx) == 1:
                    ...
                elif type(sx) == AsyncResetType:
                    ...
                elif type(sx) == ResetType:
                    ...
                else:
                    errors.append(IllegalResetType(info, target, s.name))
                
                if CheckTypes.valid_connect(s.typ, s.init.typ) is False:
                    con_msg = DefRegister(s.name, s.typ, s.clock, s.reset, s.init, NoInfo())
                    # TODO WRef class
                    errors.append(InvalidConnect(info, target, con_msg, _, s.init))
        
        def check_width_p(minfo: Info, target: str, p: Port):
            check_width_t(p.info, target, p.typ)
        
        def check_width_m(target: str, m: DefModule):
            for mk, ma in m.__dict__.items():
                if type(ma) == List[Port] and mk == 'ports':
                    for p in ma:
                        check_width_p(m.info, gen_target(target, m.name), p)
                if type(ma) == Block and mk == 'body':
                    for s in ma.stmts:
                        check_width_s(m.info, gen_target(target, m.name), s)
        
        for m in c.modules:
            check_width_m(c.main, m)
        
        errors.trigger()
        return c
