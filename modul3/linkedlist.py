class Node(object):
    """sebuah simpul di linked list"""
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def kunjungi(head):
    curNode = head
    while curNode is not None:
        print(curNode.data)
        curNode = curNode.next    

a = Node(11)
b = Node(52)
c = Node(18)

a.next=b
b.next=c




print(kunjungi(a))
print(kunjungi(b))