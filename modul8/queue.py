class queue():
    def __init__(self) -> None:
        self.item = []
    def isEmpty(self):
        print(len(self.item) == 0)
    def __len__(self):
        return len(self.item)