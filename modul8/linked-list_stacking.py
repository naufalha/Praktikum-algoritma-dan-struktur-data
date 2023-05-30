class StackLL(object):
    def __init__(self):
        self.top = None
        self.size = 0
    def isEmpty(self):
        return self.top == None
    def __len__(self):
        return self.size
    def peek(self):
        assert not self.isEmpty(), "Stack kosong. Tidak bisa diintip."
        return self.top.item
    def pop(self):
        assert not self.isEmpty(), "Stack kosong. Tidak bisa di-pop"
        node = self.top
        self.top = self.top.next
        self.size -= 1
        return node.item
    def push(self, data):
        self.top = _StackNode(data, self.top)
        self.size += 1
    def printstack(self):
        print("Isi stack: ")
        node = self.top
        while node != None:
            print(node.item, end = " ")
            node = node.next
        print()
class _StackNode(object):
    def __init__(self, data, link):
        self.item = data
        self.next = link

stacking = StackLL()
stacking.push(3)
stacking.push(2)
stacking.push(1)
print(stacking.printstack())