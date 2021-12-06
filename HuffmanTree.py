from HuffmanNode import *


# return a string binary representation
# of ASCII code for given letter
def to_binary_string(a):
    l, m = [], []
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return str(m)[1:-1]


# Holds root and methods for operating on huffman trees
class HuffmanTree:
    root = HuffmanNode()
    zeroNode = root  # node for adding new letters

    # returns node with given letter
    # returns None- if no such node is found
    def find_node(self, letter):
        return self._find_node_aux(self.root, letter)

    # returns node with given letter
    def _find_node_aux(self, node, letter):
        if node.letter == letter:
            return node

        if node.right is not None:
            n = self._find_node_aux(node.right, letter)
            if n: return n

        if node.left is not None:
            n = self._find_node_aux(node.left, letter)
            if n: return n

        return None

    def get_code_from_letter(self, letter):
        # TODO implement
        node = self.find_node(letter)

        # if letter not found
        if node is None:
            return None

        return "NOT IMPLEMENTED"

    def get_letter_from_code(self, code):
        # TODO implement
        return "NOT IMPLEMENTED"

    def add(self, letter):
        node = self.find_node(letter)

        # if letter found
        if node is not None:
            #TODO REBUILD IF NEEDED
            self.count_up(node)
            # TODO get the new letters code
            return "NOT IMPLEMENTED"

        # add new letter if not found
        self.add_new_letter(letter)
        #TODO REBUILD IF NEEDED
        return str(0) + to_binary_string(letter)

    # splits the zero node to add new letter
    def add_new_letter(self, letter):
        # adding +1 to all parents
        self.count_up(self.zeroNode)

        # left node
        self.zeroNode.left = HuffmanNode()
        self.zeroNode.left.count = 0
        self.zeroNode.left.parent = self.zeroNode

        # right node
        self.zeroNode.right = HuffmanNode()
        self.zeroNode.right.letter = letter
        self.zeroNode.right.count = 1
        self.zeroNode.right.parent = self.zeroNode

        # replacing zero node with a new one
        self.zeroNode = self.zeroNode.left

    def count_up(self, node):
        self._count_up_aux(node)

    # increments counters up the tree
    def _count_up_aux(self, node):
        node.count = node.count + 1
        if node.parent is not None:
            self._count_up_aux(node.parent)

    # count dictionary size
    # only nodes that contain letters
    def dict_size(self):
        return self._dict_size_aux(self.root)

    def _dict_size_aux(self, node):
        # TODO implement
        if node is None:
            return 0

        return "NOT IMPLEMENTED"
        # return self._dict_size_aux(node.left) + self._dict_size_aux(node.right)

    # prints the tree
    def display(self):
        print("--CURRENT TREE--")
        self.root.display()
        print()
