#!python3
from methods import io, data, math
import tokenz

import interpreter

intp = interpreter.Interpreter()

class UndefinedFunctionError(Exception): pass

def reg(it, c):
    it.valid = it.valid + [(c().methods, c())]


class Call:
    def __init__(self, method, args, doEval=True):
        self.method = method
        self.a = args
        self.de = doEval
        self.vals = []

        for t in self.a:
            self.vals.append(str(t.val))
        self.valid = []

        reg(self, io.IO)
        reg(self, data.Data)
        reg(self, math.Math)
        
        
    def run(self):

        f = False
        for m in self.valid:
            if self.method in m[0]:
                if self.method in m[1].banned:
                    f = False
                    break
                if self.de:
                    if self.method != "var":
                        args2pass = ""
                        args2pass = " ".join(self.vals)
                        args2pass = intp.eval(args2pass)
                    else:
                        args2pass = ""
                        args2pass = " ".join(self.vals)
                        a = tokenz.tokenize(args2pass)
                        args2pass = intp.eval(tokenz.detokenize(a[1:]))
                        a[0].type = "ident"
                        args2pass = [a[0]] + args2pass
                else:
                    args2pass = self.a

                return_val = m[1].funcs[m[0].index(self.method)](args2pass)
                f = True
                break
        if not f:
            return_val = None
            raise UndefinedFunctionError("Attempted to run function %s, but was undefined" % self.method)
        return return_val
