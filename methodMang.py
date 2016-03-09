from methods import output, data
import tokenz
import interpreter

intp = interpreter.Interpreter()

class UndefinedFunctionError(Exception): pass



class Call:
    def __init__(self, method, args):
        self.method = method
        self.a = args
        self.vals = []
        for t in self.a:
            self.vals.append(str(t.val))
        self.valid = []
        
        self.valid = self.valid + [(output.Output().methods, output.Output())]
        self.valid = self.valid + [(data.Data().methods, data.Data())]
        
        
    def run(self):

        f = False
        for m in self.valid:
            if self.method in m[0]:
                args2pass = ""

                args2pass = " ".join(self.vals)
                
                # print(args2pass)
                args2pass = intp.eval(args2pass)
                # print(str(args2pass) + " -- " + str(self.method))
                return_val = m[1].funcs[m[0].index(self.method)](args2pass)
                f = True
                break
        if not f:
            return_val = None
            raise UndefinedFunctionError("Attempted to run function %s, but was undefined" % self.method)
        return return_val
