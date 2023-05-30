class queue():
    def __init__(self) -> None:
        self.item = []
    def isEmpty(self):
        print(len(self.item) == 0)
    def __len__(self):
        return len(self.item)
    def enqueue(self, data):
        self.item.append(data)  
    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        return self.item.pop(0)
    
q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
q.dequeue()
q.dequeue()

for i in range(len(q)):
    print(q.dequeue())