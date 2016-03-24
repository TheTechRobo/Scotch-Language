import tokenz, interpreter

class MethodInputError(Exception): pass
class FunctionError(Exception): pass

funcs = {}

def define(args):
    if len(args) != 2: raise MethodInputError("Incorrect number of inputs, should be 2, %s were given" % len(args))
    elif args[0].type == "func" and args[1].type == "codeblock":
        funcs[str(args[0].val)] = args[1]
    else:
        raise MethodInputError("Incorrect type of arguments for function: %s, %s" % (str(args[0].type), str(args[1].type)))
    return tokenz.Token("None", None)

def call(args):
    if len(args) != 1: raise MethodInputError("Incorrect number of inputs, should be 1, %s were given" % len(args))
    elif args[0].type == "func":
        try:
            interpreter.Interpreter().call(funcs[str(args[0].val)])
        except KeyError:
            raise FunctionError("Attempted to call undefined function %s" % args[0].val[1:])
    else:
        raise MethodInputError("Incorrect type of arguments for function: %s" % str(args[0].type))
    return tokenz.Token("None", None)

class Functions():
    def __init__(self):
        self.methods = ["def", "call"]
        self.banned = ["call"]
        self.funcs = [define, call]
    
    
