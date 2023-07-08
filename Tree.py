
class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def add_element(self, new_element):
        if self.data:

            if new_element < self.data:
                if self.left is None:
                    self.left = Tree(new_element)
                else:
                    self.left.add_element(new_element)

            elif new_element > self.data:
                if self.right is None:
                    self.right = Tree(new_element)
                else:
                    self.right.add_element(new_element)

        else:
            self.data = new_element

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


root = Tree(5)
root.add_element(8)
root.add_element(11)
root.add_element(1)
root.add_element(2)
root.add_element(10)
root.add_element(12)
root.add_element(10.5)
root.add_element(13)
root.add_element(12.5)
root.add_element(11.5)

root.print_tree()
