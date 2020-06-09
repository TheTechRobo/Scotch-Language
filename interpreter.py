#!python3
import tokenz
import methodMang
import sys  

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
        x = l.replace("\n", "")
        c[i] = x.replace("\t", "")
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
                    
                    if len(self.tokens) > 2:
                        if self.tokens[1].val == "(":
                            i = 1
                            d = 1
                            while True:
                                i+= 1
                                if self.tokens[i].val == "(":
                                    d += 1
                                elif self.tokens[i].val == ")":
                                    d -= 1
                                    if d == 0:
                                        break
                            that = self.tokens[1:i+1]
                            that[0] = tok
                            that.pop()  # Get rid of )
                            methodMang.Call("call", that, True, False).run()
                            self.tokens = self.tokens[i+2:]
                            returns.append(tokenz.Token("None", None))
                    
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

if len(sys.argv) > 1:
    with open(sys.argv[1], "r") as openedFile:
        print("Scotch Programming Language v0.1.9")
        print("Created by Daniel (Icely) 2016\n")
        for line in openedFile:
            from importlib import reload
            reload(methodMang)
            if "#!" in line:
                continue
            try: 
                code = line
                if code == "kill":
                    print("Program killed")
                    break
                else:
                    Interpreter().eval(code)
            except KeyboardInterrupt:
                pass
            except Exception as e:
                print("ERROR: %s; %s" % (e.__class__.__name__, str(e)))
                if input("Raise? (Y/n) ") in "Yy": raise e
            sys.exit("Execution completed")
if __name__ == "__main__":
    print("Scotch Programming Language v0.1.9")
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
