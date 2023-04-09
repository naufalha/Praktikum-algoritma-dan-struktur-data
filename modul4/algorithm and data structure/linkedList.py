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

    def add_node_in_middle(self, prev_data, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current is not None:
            if current.data == prev_data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

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
        string = ""
        current = self.head
        while current is not None:
            if current.next != None:
                string += str(current.data) + " --> "
                current = current.next
            else:
                string += str(current.data)
                current = current.next
                
        print(string)


    def count_nodes(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


data = ["nopal","vem","lecrec","hamilton","maxverstappen","binnoto"]
my_list = LinkedList()

##menambahkan data dari belakang
for i in data:
    my_list.insertAtEnd(i)




my_list.print_list()

##menambahkan data dari depan
my_list.insertAtStart("lewis")

##menambahkan data di tengah
my_list.add_node_in_middle("lecrec","sebastian")

##menghapus data
my_list.delete("binnoto")
##menghapus node yang tidak ada
my_list.delete("russel")

#menampilkan node
my_list.print_list()

#menghitung jumlah node
print(my_list.count_nodes())
#membalikkan node
my_list.reverse()
my_list.print_list()


print("=========================================")
print("L200210135 - Naufal Hanief Mafaza")