class PriorityQueue(object):
    def __init__(self) -> None:
        self.qlist = []
    def __len__(self):
        return len(self.qlist)
    def isEmpty(self):
        return len(self) == 0
    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)
    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        max = 0
        for i in range(len(self.qlist)):
            if self.qlist[i].priority < self.qlist[max].priority:
                max = i
        hasil = self.qlist[max].item
        del self.qlist[max]
        return hasil
    
class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority

s = PriorityQueue()
s.enqueue("jeruk", 4)
s.enqueue("tomat", 2)
s.enqueue("mangga", 0)
s.enqueue("duku", 5)
s.enqueue("pepaya", 2)

for i in range(len(s)):
    print(s.dequeue())