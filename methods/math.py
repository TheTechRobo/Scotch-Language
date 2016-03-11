#!python3
import tokenz

class MethodInputError(Exception): pass
class VariableError(Exception): pass

def all_type(toks, t):
    for tok in toks:
        if tok.type == "value":
            if type(tok.val) != int:
                return False
        elif tok.type != t:
            return False
    return True

def add(args):
    if len(args) < 2: raise MethodInputError("Incorrect number of inputs, should be at least 2, %s were given" % len(args))
    elif not all_type(args, "numb"): raise MethodInputError("Incorrect type of arguments for function, should be all NUMB")
    else:
        total = 0
        for tok in args:
            total = total + tok.val
        return tokenz.Token("numb", total)
    
def sub(args):
    if len(args) < 2: raise MethodInputError("Incorrect number of inputs, should be at least 2, %s were given" % len(args))
    elif not all_type(args, "numb"): raise MethodInputError("Incorrect type of arguments for function, should be all NUMB")
    else:
        total = args[0]
        for tok in args[1:]:
            total = total - tok.val
        return tokenz.Token("numb", total)

def mul(args):
    if len(args) < 2: raise MethodInputError("Incorrect number of inputs, should be at least 2, %s were given" % len(args))
    elif not all_type(args, "numb"): raise MethodInputError("Incorrect type of arguments for function, should be all NUMB")
    else:
        total = 1
        for tok in args:
            total = total * tok.val
        return tokenz.Token("numb", total)
    
def div(args):
    if len(args) < 2: raise MethodInputError("Incorrect number of inputs, should be at least 2, %s were given" % len(args))
    elif not all_type(args, "numb"): raise MethodInputError("Incorrect type of arguments for function, should be all NUMB")
    else:
        total = args[0]
        for tok in args[1:]:
            total = total / tok.val
        return tokenz.Token("numb", total)
    
def power(args):
    if len(args) != 2: raise MethodInputError("Incorrect number of inputs, should be 2, %s were given" % len(args))
    elif not all_type(args, "numb"): raise MethodInputError("Incorrect type of arguments for function, should be all NUMB")
    else:
        return tokenz.Token("numb", pow(args[0].val, args[1].val))


class Math:
    def __init__(self):
        self.methods = ["add", "sub", "mul", "div", "pow"]
        self.banned = []
        self.funcs = [add, sub, mul, div, power]
