import operator

ops = {
    "+": (operator.add, 1),
    "-": (operator.sub, 1),
    "*": (operator.mul, 2),
    "/": (operator.truediv, 2),
    "(": (None, 4),
    ")": (None, 4),
    "^": (operator.pow, 3)
}

symb = {
    "e": "2.718281828459",
    "p": "3.14"
}

class Stack:
    def __init__(self, inp = []):
        self.data = inp
    
    def Head(self):
        return self.data[len(self.data)-1]

    def Pop(self):
        item = self.data.pop(len(self.data)-1)
        return item
    
    def Push(self, item):
        self.data.append(item)

class Queue:
    def __init__(self, inp = []):
        self.data = inp
    
    def Head(self):
        return self.data[0]

    def Pop(self):
        item = self.data.pop(0)
        return item
    
    def Push(self, item):
        self.data.append(item)
         
def stringToList(inp):
    txt = ""
    new = []
    for i in inp:
        if not i.isspace():
            if i.isnumeric() or i == ".":
                txt+=i
            else:
                if txt:
                    new.append(txt)
                txt = ""
                if i in symb:
                    new.append(symb[i])
                else:
                    new.append(i)
    if txt:
        new.append(txt)
    return new

def ShuntingYard(inp):
    def unpackParantheses(stack, queue):
        for i in reversed(list(stack.data)):
            if i == ")":
                stack.Pop()
                unpackParantheses(stack, queue)
            elif i == "(":
                stack.Pop()
                return
            else:
                item = stack.Pop()
                queue.Push(item)

    inp = stringToList(inp)
    stack = Stack()
    queue = Queue()
    for i in inp:
        if i.isnumeric() or isFloat(i):
            queue.Push(i)
        elif i == ")":
            unpackParantheses(stack, queue)
        elif i == "(":
            stack.Push(i)
        elif i in ops:
            if not stack.data:
                stack.Push(i)
            elif ops[i][1] > ops[stack.Head()][1] or stack.Head() == "(":
                stack.Push(i)
            else: 
                queue.Push(stack.Pop())
                stack.Push(i)
        else:
            print(i, "Is not a valid operator/number")
            return
    for i in range(len(stack.data)):
        queue.Push(stack.Pop())
    return queue

def isFloat(x):
    try:
        float(x)
        return True
    except ValueError:
        False

def Calc(inp):
    inp = ShuntingYard(inp)
    if inp == None:
        return
    output = Stack([])
    while True:
        i = inp.Pop()
        if str(i).isnumeric() or isFloat(i):
            output.Push(i)
        else:
            x = output.Pop()
            output.Push(ops[i][0](float(output.Pop()), float(x)))
        if not inp.data:
            return output.data[0]

def VPrism(l,b,h):
    return l*b*h

def OPrism(l,b,h):
    return 2*(2*(l+b+h))

def ACircle(r): 
    return (r**2)*3.4

def OCircle(r):
    return (2*3.14*r)

def ACircle(r):
    return 3.14*(r**2)

def OCyllinder(r,h):
    return Calc()

def AKule(r):
    return 4*3.14*(r**2)

def VKule(r):
    return (4/3)*3.14*(r**3)