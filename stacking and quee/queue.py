class   queue:
    def __init__(self) -> None:
        self.item = []
    def enqueue(self, value):
        self.item.append(value)
    def dequeue(self):
        if len(self.item) == 0:
            print("Queue is empty")
            return None
        else:
            return self.item.pop(0)
    def size(self):
        xx=0
        for i in range (len(self.item)):
            xx+=1
        return xx