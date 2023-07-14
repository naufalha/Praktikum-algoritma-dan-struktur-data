class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_transversal(root):
    if root:
        inorder_transversal(root.left)
        print(root.data, end=' ')
        inorder_transversal(root.right)
        
def bulid_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    
    return root

inorder_transversal(bulid_tree())

                    