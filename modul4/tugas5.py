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
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

   
    def search(self, key):
        curr_node = self.head
        while curr_node:
            if curr_node.data == key:
                print(key, "ditemukan")
                return True
            curr_node = curr_node.next
        print(key,"tidak ditemukan")
        return False


data = ["nopal","vem","lecrec","hamilton","maxverstappen","binnoto"]
my_list = LinkedList()
for i in data:
    my_list.append(i)

my_list.search("binnoto")
my_list.search("ferrari wordl champ")


print("_______________________________")
print("l200210135 Naufal Hanief Mafaza")

