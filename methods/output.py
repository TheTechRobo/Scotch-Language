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
        return return tokenz.Token("None", None)
    
class Output:
    def __init__(self):
        self.methods = ["out"]
        self.funcs = [out]
    




    
    

    
