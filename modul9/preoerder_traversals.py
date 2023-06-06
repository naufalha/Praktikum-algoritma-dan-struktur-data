def preorder_traversal(subpohon):
    if subpohon is not None:
        print(subpohon.data)
        preorder_traversal(subpohon.kiri)
        preorder_traversal(subpohon.kanan)