from HuffmanNode import *


# Holds root and methods for operating on huffman trees
class HuffmanTree:
    def __init__(self):
        self.root = HuffmanNode()
        self.zeroNode = self.root  # node for adding new letters

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
        node = self.find_node(letter)

        # if letter not found
        if node is None:
            return None

        curr_node = node
        curr_parent = node.parent
        code = ""
        while curr_parent is not None:
            if curr_node == curr_parent.left:
                code = "0" + code
            else:
                code = "1" + code

            curr_node = curr_parent
            curr_parent = curr_parent.parent

        return code

    def get_letter_from_code(self, code):
        curr_node = self.root

        while code != "":
            # letter not found
            if curr_node is None:
                return None

            direction = code[0]

            if direction == "1":
                curr_node = curr_node.right
            if direction == "0":
                curr_node = curr_node.left

            code = code[1:]

        return curr_node.letter

    # returns code of added letter if already exists
    # and -1 if it was freshly inserted
    def add(self, letter):
        node = self.find_node(letter)

        # if letter found
        if node is not None:
            self.count_up(node)
            return self.get_code_from_letter(letter)

        # add new letter if not found
        self.add_new_letter(letter)
        # TODO REBUILD IF NEEDED
        return -1

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

#NEW THINGIES woj:

    def get_node_zero_code(self):
        node = self.zeroNode

        # if letter not found
        if node is None:
            return None

        curr_node = node
        curr_parent = node.parent
        code = ""
        while curr_parent is not None:
            if curr_node == curr_parent.left:
                code = "0" + code
            else:
                code = "1" + code

            curr_node = curr_parent
            curr_parent = curr_parent.parent


        return code
