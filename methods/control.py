import tokenz, interpreter

class MethodInputError(Exception): pass

def valueify(args):
    x = []
    for t in args:
        if t.type == "value":
            y = tokenz.tokenize(t.val)[0]
            x.append(y)
        else:
            x.append(t)
    return x

def ifstm(args):
    args = valueify(args)
    if len(args) != 2: raise MethodInputError("Incorrect number of inputs, should be 2, %s were given" % len(args))
    elif args[0].type == "bool" and args[1].type == "codeblock":
        if args[0].val:
            interpreter.Interpreter().call(args[1])
    else:
        raise MethodInputError("Incorrect type of arguments for function: %s, %s" % (str(args[0].type), str(args[1].type)))
    return tokenz.Token("None", None)

def ifelse(args):
    args = valueify(args)
    if len(args) != 3: raise MethodInputError("Incorrect number of inputs, should be 3, %s were given" % len(args))
    elif args[0].type == "bool" and args[1].type == "codeblock":
        if args[0].val:
            interpreter.Interpreter().call(args[1])
        else:
            interpreter.Interpreter().call(args[2])
    else:
        raise MethodInputError("Incorrect type of arguments for function: %s, %s, %s" % (str(args[0].type), str(args[1].type), str(args[2].type)))
    return tokenz.Token("None", None)

def rep(args):
    args = valueify(args)
    if len(args) != 2: raise MethodInputError("Incorrect number of inputs, should be 2, %s were given" % len(args))
    elif args[0].type == "numb" and args[1].type == "codeblock":
        for n in range(args[0].val):
            interpreter.Interpreter().call(args[1])
    else:
        raise MethodInputError("Incorrect type of arguments for function: %s, %s" % (str(args[0].type), str(args[1].type)))
    return tokenz.Token("None", None)

class Control():
    def __init__(self):
        self.methods = ["if", "ifelse", "repeat"]
        self.banned = []
        self.funcs = [ifstm, ifelse, rep]

