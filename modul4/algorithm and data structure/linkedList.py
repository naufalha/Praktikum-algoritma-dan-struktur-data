class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insertAtStart(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
    def count_nodes(head):
        count = 0
        current = head
        while current is not None:
            count += 1
            current = current.next
        return count

data = ["nopal","vem","lecrec","hamilton","maxverstappen","binnoto"]
my_list = LinkedList()
for i in data:
    my_list.insertAtEnd(i)

my_list.print_list()