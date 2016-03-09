#!python3
import tokenz
class MethodInputError(Exception): pass

data = {}

def var(args):
    if args[0].type == "call" and (args[1].type != "call"):
        data[args[0].val] = args[1]
    else:
        raise MethodInputError("Incorrect type of arguments for function: %s & %s" % (str(args[0].type), str(args[1].type)) )
    
    return tokenz.Token("None", None)

def get(args):
    if args[0].type == "call":

        return data[args[0].val] # Token obj
    else:
        return tokenz.Token("None", None)

class Data:
    def __init__(self):
        self.methods = ["var", "get"]
        self.funcs = [var, get]
