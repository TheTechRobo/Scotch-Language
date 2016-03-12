#!python3
import tokenz

class MethodInputError(Exception): pass
class ConversionError(Exception): pass

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

def toInt(args):
    if len(args) != 1: raise MethodInputError("Incorrect number of inputs, should be 1, %s were given" % len(args))
    if args[0].type == "numb":
        return args[0]
    else:
        try:
            return tokenz.Token("numb", int(args[0].val))
        except ValueError:
            raise ConversionError("Attempted to convet %s type to numb" % str(args[0].type))

def toBool(args):
    if len(args) != 1: raise MethodInputError("Incorrect number of inputs, should be 1, %s were given" % len(args))
    if args[0].type == "bool":
        return args[0]
    else:
        val = args[0].val
        if "False" in val:
            val = False
        elif "True" in val:
            val = True
        elif val == 0:
            val = False
        elif val == 1:
            val = True
        else:
            val = False
        return tokenz.Token("bool", val)


def bNot(args):
    if len(args) != 1: raise MethodInputError("Incorrect number of inputs, should be 1, %s were given" % len(args))
    if args[0].type == "bool":
        return tokenz.Token("bool", not args[0].val)
    else:
        raise MethodInputError("Incorrect type of arguments for function: %s" % str(args[0].type))
  

class Types:
    def __init__(self):
        self.methods = ["concat", "upper", "lower", "str", "numb", "bool", "!"]
        self.banned = []
        self.funcs = [concat, upper, lower, toString, toInt, toBool, bNot]
