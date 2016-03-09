#!python3
from methods import io, data
import tokenz

import interpreter

intp = interpreter.Interpreter()

class UndefinedFunctionError(Exception): pass

def reg(it, c):
    it.valid = it.valid + [(c().methods, c())]


class Call:
    def __init__(self, method, args):
        self.method = method
        self.a = args
        self.vals = []

        for t in self.a:
            self.vals.append(str(t.val))
        self.valid = []

        reg(self, io.IO)
        reg(self, data.Data)
        
        
    def run(self):

        f = False
        for m in self.valid:
            if self.method in m[0]:
                args2pass = ""

                args2pass = " ".join(self.vals)

                args2pass = intp.eval(args2pass)

                return_val = m[1].funcs[m[0].index(self.method)](args2pass)
                f = True
                break
        if not f:
            return_val = None
            raise UndefinedFunctionError("Attempted to run function %s, but was undefined" % self.method)
        return return_val
