class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def sum_list(self):
        total = 0
        current_node = self.head
        while current_node is not None:
            total += current_node.data
            current_node = current_node.next

        return total

# create a linked list with 6 nodes
my_list = LinkedList()
my_list.append(3)
my_list.append(5)
my_list.append(2)
my_list.append(6)
my_list.append(9)
my_list.append(7)





# compute the sum of the list
list_sum = my_list.sum_list()
print("Sum of the linked list:", list_sum)
