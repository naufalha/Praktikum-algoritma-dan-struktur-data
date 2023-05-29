class stack():
    def __init__(self) -> None:
        self.item = []
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
            
    
        

stacking = stack()
stacking.push("iqbal")
stacking.push("julian")
print(stacking.size())