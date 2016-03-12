import re

NUM = re.compile(r"(?:-)?\d+(\.\d+)?")
STR = re.compile(r"(\".*?\")")
BOOL = re.compile(r"True|False")
CALL = re.compile(r"[0-9a-zA-Z!#$%&+,./:;<>?@\\^_|~-]+")
FUNC = re.compile(r"\*[a-zA-Z!#$%&+,./:;<>?@\\^_|~-]+")


class TokenizeErr(Exception): pass


class Token:
    def __init__(self, type, val):
        self.type = type
        self.val = val
        
    def __repr__(self):
        if self.type == 'array':
            return "[ " + ' '.join(map(str, self.val)) + " ]"
        return repr(str(self.val) + "." + str(self.type))

def stringify(t):
    return "\"" + str(t) + "\""
def destringify(t):
    if t.type == "str":
        return t.val[1:-1]
    elif t.type == "value":
        return destringify(tokenize(t.val)[0])
    else:
        return t.val
def tokenize(code):

    tokens = []
    code = str(code)
    while code:
        numm = NUM.match(code)
        strm = STR.match(code)
        boolm = BOOL.match(code)
        callm = CALL.match(code)
        funcm = FUNC.match(code)

        if numm:
            sp = numm.span()[1]
            
            n = code[:sp]
            try:
                n = int(n)
            except ValueError:
                n = float(n)
            except ValueError:
                break
            tokens.append(Token('numb', n))
            code = code[sp:]
        elif strm:
            sp = strm.span()[1]
            s = code[:sp]
            tokens.append(Token("str", s))
            code = code[sp:]
        elif boolm:
            sp = boolm.span()[1]
            b = code[:sp]
            if b == "True":
                b = True
            else:
                b = False
            code = code[sp:]
            tokens.append(Token("bool", b))
        elif callm:
            sp = callm.span()[1]
            name = code[:sp]
            code = code[sp:]
            tokens.append(Token("call", name))

        elif funcm:
            sp = funcm.span()[1]
            name = code[:sp]
            code = code[sp:]
            tokens.append(Token("func", name))

        elif code[0] == "(":
            code = code[1:]

            tokens.append(Token("paren-o", "("))
            ind = 1
            i = 0
            for c in code:
                if ind == 0:
                    break
                if c == "(":
                    ind += 1
                elif c == ")":
                    ind -= 1
                i += 1
            tokens = tokens + tokenize(code[0:i-1])
            tokens.append(Token("paren-c", ")"))
            code = code[i+1:]

        elif code[0] == "{":
            ind = 1
            i = 1
            for c in code[1:]:
                if ind == 0:
                    break
                if c == "{":
                    ind += 1
                elif c == "}":
                    ind -= 1
                i += 1
            tokens.append(Token("codeblock", code[0:i]))
            code = code[i:]    
            
        elif code[0] == " ":
            code = code[1:]
        else:
            raise TokenizeErr("Not a reconized token! Got %s" % code)
        
    return tokens

def detokenize(tokens):
    vals = []
    for tok in tokens:
        vals.append(str(tok.val))
    return " ".join(vals)

if __name__ == "__main__":
        while True:
                c = input("Code: ")
                for t in tokenize(c):
                        print(t)
                      
