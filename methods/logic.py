import tokenz

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

def andStm(args):
    args = valueify(args)
    if len(args) != 2: raise MethodInputError("Incorrect number of inputs, should be 2, %s were given" % len(args))
    elif args[0].type == "bool" and args[1].type == "bool":
        return tokenz.Token("bool", args[0].val and args[1].val)
    else:
        raise MethodInputError("Incorrect type of arguments for function: %s, %s" % (str(args[0].type), str(args[1].type)))
        return tokenz.Token("None", None)

def orStm(args):
    args = valueify(args)
    if len(args) != 2: raise MethodInputError("Incorrect number of inputs, should be 2, %s were given" % len(args))
    elif args[0].type == "bool" and args[1].type == "bool":
        return tokenz.Token("bool", args[0].val or args[1].val)
    else:
        raise MethodInputError("Incorrect type of arguments for function: %s, %s" % (str(args[0].type), str(args[1].type)))
        return tokenz.Token("None", None)

def notStm(args):
    if len(args) != 1: raise MethodInputError("Incorrect number of inputs, should be 1, %s were given" % len(args))
    if args[0].type == "bool":
        return tokenz.Token("bool", not args[0].val)
    else:
        raise MethodInputError("Incorrect type of arguments for function: %s" % str(args[0].type))


def eq(args):
    args = valueify(args)
    if len(args) != 2: raise MethodInputError("Incorrect number of inputs, should be 2, %s were given" % len(args))
    return tokenz.Token("bool", args[0].val == args[1].val)

def greater(args):
    args = valueify(args)
    if len(args) != 2: raise MethodInputError("Incorrect number of inputs, should be 2, %s were given" % len(args))
    elif args[0].type == "numb" and args[1].type == "numb":
        return tokenz.Token("bool", args[0].val > args[1].val)
    else:
        raise MethodInputError("Incorrect type of arguments for function: %s, %s" % (str(args[0].type), str(args[1].type)))
        return tokenz.Token("None", None)

def less(args):
    args = valueify(args)
    if len(args) != 2: raise MethodInputError("Incorrect number of inputs, should be 2, %s were given" % len(args))
    elif args[0].type == "numb" and args[1].type == "numb":
        return tokenz.Token("bool", args[0].val < args[1].val)
    else:
        raise MethodInputError("Incorrect type of arguments for function: %s, %s" % (str(args[0].type), str(args[1].type)))
        return tokenz.Token("None", None)

class Logic():
    def __init__(self):
        self.methods = ["and", "or", "!", "equal", "greater", "less"]
        self.banned = []
        self.funcs = [andStm, orStm, notStm, eq, greater, less]
