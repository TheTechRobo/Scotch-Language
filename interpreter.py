import tokenz
import methodMang
import time


time.sleep(3)

class Interpreter:

    def __init__(self):
       self.tokens = ""
       self.pos = 0

    def crunch(self):
        self.pos += 1
        return self.tokens.pop(0)

    def get_args(self, toks): #Function arg getter, input a list of tokens like... out (123 456) ... and  will return [123, 456]
        # print("Get_args toks passed: " + str(toks))
        t = toks
        t_vals = []
        for t_ in t:
            t_vals.append(t_.val)
       #  print("t_vals: "+str(t_vals))
        if "(" not in t_vals:
            # print("Not a func")
            return ("notAfunc", t[1:], t[0])
        self.crunch()
        indt = 0
        u = 0
        while t.pop(0).val != "(":
            pass
        while True:
            if t[indt].val == "(": u += 1
            if t[indt].val == ")" and u > 0: u -= 1
            indt += 1
            if t[indt].val == ")" and u == 0:
                break
            
        if (indt == 0):
            return ([t[0]], t[1:])
        else:   
            return (t[0:indt], t[indt+1:])
                
    
    def eval(self, code): # Code is string...
        self.tokens = tokenz.tokenize(str(code))
        # print("%s tokenized = %s" %(code, str(self.tokens)))
        self.pos = 0
        returns = []
        while self.tokens != []:
            try:
                tok = self.tokens[self.pos]
                if tok.type == "call":
                    
                    args = self.get_args(self.tokens)
                    # print("args got: %s" % str(args))
                    if args[0] == "notAfunc":
                        self.tokens = args[1]
                        returns.append(args[2])
                        # print("Not a func, appending %s" % str(args[2].val))
                    else:
                        self.tokens = args[1]
                        returns.append(methodMang.Call(tok.val, args[0]).run())
                        
                elif tok.type == "numb":
                    self.crunch()
                    
                    returns.append(tok)      
                elif tok.type == "str":
                    self.crunch()
                    
                    returns.append(tok)
                elif tok.type == "bool":
                    self.crunch()
                    
                    returns.append(tok)
            except IndexError:
                break
        # print(returns)
        return returns

                    
if __name__ == "__main__":
    print("Scotch Programming Language")
    print("Created by Daniel Sage 2016")
    print("Running Interactive prompt... \n")
    while True:
        try:
            code = input(">>> ")
            if code == "kill":
                break
            Interpreter().eval(code)
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print("ERROR: %s; %s" % (e.__class__.__name__, str(e)))
        
