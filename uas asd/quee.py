class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def pop(self):
        print(len(self.items))
        return self.items[len(self.items)-1]
    
antri = Queue()
antri.enqueue('A')
antri.enqueue('B')
antri.enqueue('C')
antri.enqueue('D')
print(antri.pop())