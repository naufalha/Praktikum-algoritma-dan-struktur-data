class stack():
    def __init__(self) -> None:
        self.item = []
    def isEmpty(self):
        return len(self.item) == 0
    def __len__(self):
        return len(self.item)
    def pop(self):
        if len(self.item) == 0:
            print("Stack is empty")
            return None
        else:
            return self.item.pop()
    def push(self, value):
        self.item.append(value)
    def size(self):
        xx=0
        for i in range (len(self.item)):
            xx+=1
        return xx
    
    def peek(self):
        if len(self.item) == 0:
            print("Stack is empty")
            return None
        else:
            return self.item[-1]
                
PROMPT = "Masukan bilangan positif(0 untuk mengakhiri)"
myStack = stack()
value = int(input(PROMPT))
while value > 0:
    myStack.push(value)
    value = int(input(PROMPT))
while not myStack.isEmpty():
    value = myStack.pop()
    print(value)
            
            