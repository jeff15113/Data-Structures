class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if (value <= self.value):
            if(self.left is None):
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        elif (value > self.value):
            if(self.right is None):
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        pass

    def get_max(self):
        # If self.right is None: self.right = maxvalue
        # if self.right is not None: check next node
        pass

    def for_each(self, cb):
        pass


tree = BinarySearchTree(5)

tree.insert(3)
