#!python3
import tokenz
import methodMang

def _2list(x):
    if type(x) == list:
        return x
    else:
        return [x]

def openFile():
    path = input("Path please: ")
    f = open(path, 'r')
    c = []
    for line in f:
        c.append(line)
    for i, l in enumerate(c):
        c[i] = l.replace("\n", "")
    c = " ".join(c)
    print("----")
    f.close()
    return c

class Interpreter:

    def __init__(self):
       self.tokens = ""
       self.pos = 0

    def crunch(self):
        self.pos += 1
        return self.tokens.pop(0)

    def func(self, toks):
        t = toks
        t_vals = []
        for t_ in t:
            t_vals.append(t_.val)
        if not "(" in t_vals or len(toks) == 1:
            return (False, t)
        if t[0].type == "call" and t[1].val != "(":
            return (False, t)
        for i, tok in enumerate(t):
            if "call" in tok.type:
                try:
                    
                    if t[i+1].val == "(":
                        u = 0
                        indt = i + 2

                        while True:
                            if t[indt].val == "(": u += 1
                            if t[indt].val == ")" and u > 0: u -= 1
                            indt += 1
                            if t[indt].val == ")" and u == 0:
                                break

                        if i+2 == indt-1:
                            return (True, t[indt+1:], t[i+2])
                        else:
                            return (True, t[indt+1:], t[i+2:indt])
                    else:
                        t[i].type = "!call"


                except IndexError:
                    return (False, [])
            else:
                pass
      
    
    def eval(self, code): # Code is string...
        self.tokens = tokenz.tokenize(str(code))
        self.pos = 0
        returns = []
        while self.tokens != []:
            try:
                tok = self.tokens[0]
                if tok.type == "call":
                    
                    args = self.func(self.tokens) # [isFunction, resulting token stream, arguments]

                    if not args[0]:
                        self.tokens = args[1][1:]

                        that = tokenz.Token("ident", args[1][0].val)
                        that.id = args[1][0].val

                        this = tokenz.Token("value", methodMang.Call("get", [that], True, False).run().val)
                        returns.append(this)
                    else: 
                        returns.append(methodMang.Call(tok.val, _2list(args[2]), False).run())
                        self.tokens = args[1]
                elif tok.type == "codeblock":
                    self.crunch()
                    
                    returns.append(tok)
                elif tok.type == "ident":
                    self.crunch()
                    
                    returns.append(tok)                  
                elif tok.type == "numb":
                    self.crunch()
                    
                    returns.append(tok)      
                elif tok.type == "str":
                    self.crunch()
                    
                    returns.append(tok)
                elif tok.type == "bool":
                    self.crunch()
                    
                    returns.append(tok)
                elif tok.type == "func":
                    self.crunch()
                    
                    returns.append(tok)
                elif tok.type == "codeblock":
                    self.crunch()
                    
                    returns.append(tok)
                
            except IndexError:
                break
        return returns

    def call(self, codeblock):
        code = codeblock.val[1:-1]
        return self.eval(code)

                    
if __name__ == "__main__":
    print("Scotch Programming Language v0.1.8")
    print("Created by Daniel (Icely) 2016")
    print("Running Interactive prompt... \n")
    while True:
        try:
            code = input(">>> ")
            if code == "kill":
                break
            elif code == "open":
                Interpreter().eval(openFile())
            else:
                Interpreter().eval(code)
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print("ERROR: %s; %s" % (e.__class__.__name__, str(e)))
            if input("Raise? (Y/n) ") in "Yy": raise e            
