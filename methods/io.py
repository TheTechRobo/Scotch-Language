#!python3
import tokenz

class MethodInputError(Exception): pass

def out(args): #[Token("num", 5), Token("num", 6)]
        
    if len(args) != 1: raise MethodInputError("Expected 1 input, got %s. %s" % (len(args), args))
    a = args[0] #easier for typing
    
    if a.type == "str":
        print(a.val[1:-1])
    elif a.type in "numbbool":
        print(str(a.val))
    else:
        raise MethodInputError("Unreconized type to outupt: %s" % a.type)
    return tokenz.Token("None", None)

def ask(args):
    if len(args) != 1: raise MethodInputError("Expected 1 input, got %s. %s" % (len(args), args))
    if args[0].type == "str":
        return tokenz.Token("str", "\""+str(input(args[0].val[1:-1] + "\n"))+"\"")
    else:
        raise MethodInputError("Incorrect type of arguments for function: %s" % str(args[0].type))
    return tokenz.Token("None", None)
    
class IO:
    def __init__(self):
        self.methods = ["out", "ask"]
        self.funcs = [out, ask]
    




    
    

    
