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
                
    def palindrom(self,text):
        for i in text:
            self.push(i)
        reversed_text = ""
        for i in range(len(text)):
            reversed_text += self.pop()
        if text == reversed_text:
            print("palindrom")
        else:
            print("bukan palindrom")
        

stacking = stack()
stacking.palindrom("julian")

