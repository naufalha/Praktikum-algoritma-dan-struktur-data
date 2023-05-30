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