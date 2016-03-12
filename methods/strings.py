#!python3
import tokenz

class MethodInputError(Exception): pass

def concat(args):
    if len(args) < 2: raise MethodInputError("Incorrect number of inputs, should be at least 2, %s were given" % len(args))
    else:
        total = ""
        for tok in args:
            if tok.type == "str":
                total += str(tok.val[1:-1])
            else:
                total += str(tok.val)
        return tokenz.Token("str", tokenz.stringify(total))

def upper(args):
    if len(args) != 1: raise MethodInputError("Incorrect number of inputs, should be 1, %s were given" % len(args))
    if args[0].type == "str":
        return tokenz.Token("str", args[0].val.upper())
    else:
        return tokenz.Token("str", tokenz.stringify(str(args[0].val).upper()))

def lower(args):
    if len(args) != 1: raise MethodInputError("Incorrect number of inputs, should be 1, %s were given" % len(args))
    if args[0].type == "str":
        return tokenz.Token("str", args[0].val.lower())
    else:
        return tokenz.Token("str", tokenz.stringify(str(args[0].val).lower()))
    
def toString(args):
    if len(args) != 1: raise MethodInputError("Incorrect number of inputs, should be 1, %s were given" % len(args))
    if args[0].type == "str":
        return args[0]
    else:
        return tokenz.Token("str", tokenz.stringify(str(args[0].val)))

class Strings:
    def __init__(self):
        self.methods = ["concat", "upper", "lower", "str"]
        self.banned = []
        self.funcs = [concat, upper, lower, toString]
