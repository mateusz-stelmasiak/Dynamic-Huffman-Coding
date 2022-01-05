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

        while len(code) != 0:
            # letter not found
            if curr_node is None:
                return ""

            direction = code[0]

            if direction == "1":
                curr_node = curr_node.right
            if direction == "0":
                curr_node = curr_node.left

            code = code[1:]

        if curr_node is None:
            return ""

        return curr_node.letter

    # returns code of added letter if already exists
    # and -1 if it was freshly inserted
    def add(self, letter):
        node = self.find_node(letter)

        # if letter found
        if node is not None:
            self.count_up(node)
            self.update(node)
            return self.get_code_from_letter(letter)

        # add new letter if not found
        node = self.add_new_letter(letter)
        self.update(node)
        return -1

    # splits the zero node to add new letter
    def add_new_letter(self, letter):
        # adding +1 to all parents
        self.count_up(self.zeroNode)

        # left node
        self.zeroNode.left = HuffmanNode()
        self.zeroNode.left.count = 0
        self.zeroNode.left.parent = self.zeroNode
        self.zeroNode.left.rank = self.zeroNode.rank - 2

        # right node
        self.zeroNode.right = HuffmanNode()
        self.zeroNode.right.letter = letter
        self.zeroNode.right.count = 1
        self.zeroNode.right.parent = self.zeroNode
        curr_node = self.zeroNode.right
        self.zeroNode.right.rank = self.zeroNode.rank - 1

        # replacing zero node with a new one
        self.zeroNode = self.zeroNode.left

        return curr_node

    def count_up(self, node):
        self._count_up_aux(node)

    # increments counters up the tree
    def _count_up_aux(self, node):
        node.count = node.count + 1
        if node.parent is not None:
            self._count_up_aux(node.parent)

    def count_down(self, node):
        self._count_down_aux(node)

    # increments counters up the tree
    def _count_down_aux(self, node):
        node.count = node.count - 1
        if node.parent is not None:
            self._count_down_aux(node.parent)

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

    def switch_nodes(self, first_node, second_node):
        # switch ranks
        first_node_rank_temp = first_node.rank
        first_node.rank = second_node.rank
        second_node.rank = first_node_rank_temp

        is_first_left_child = first_node.parent.left == first_node
        is_sec_left_child = second_node.parent.left == second_node
        if is_first_left_child:
            if is_sec_left_child:
                first_node.parent.left, second_node.parent.left = second_node, first_node
            else:
                first_node.parent.left, second_node.parent.right = second_node, first_node
        # first right
        else:
            if is_sec_left_child:
                first_node.parent.right, second_node.parent.left = second_node, first_node
            else:
                first_node.parent.right, second_node.parent.right = second_node, first_node

        # lastly, switch parents
        first_node.parent, second_node.parent = second_node.parent, first_node.parent

    def recalculate_counts(self):
        levels = self.BFS()

        # last level
        level_index = len(levels) - 1

        while level_index != 0:
            for node in levels[level_index]:
                parent = node.parent
                # get only empty nodes
                if parent.letter is None:
                    parent.count = parent.left.count + parent.right.count

            level_index = level_index - 1

    def get_same_count(self, levels, node_level, node_count):
        for i in range(0, node_level):
            for node in levels[i]:
                if node.count == node_count:
                    return node

        return None


    def update(self, updated_node):
        levels = self.BFS()

        while not self.check_for_vitter_rule():
            print("TREE BREAKS RULE")
            self.display()

            node_level = self.get_block_index(levels, updated_node)
            # it wasn't the inserted that broke the rule
            broken_level, broken_level_index = self.get_block_index_breaking_vitter_rule()

            if broken_level_index == node_level or broken_level_index == node_level - 1:
                # swap_level = node_level - 1
                # swap_max = len(levels[swap_level]) - 1
                switch_candidate = self.get_same_count(levels, node_level, updated_node.count - 1)
                self.switch_nodes(updated_node, switch_candidate)
            else:
                self.switch_nodes(broken_level[0], broken_level[1])

            self.recalculate_counts()
            print("AFTER SWITCH")
            self.display()

    # if no block breaks, returns none
    def get_block_index_breaking_vitter_rule(self):
        # get block
        block_list = self.BFS()
        for index, block in enumerate(block_list):
            for node_id in range(1, len(block)):
                if block[node_id].count < block[node_id - 1].count:
                    return block, index

        return None

    def check_for_vitter_rule(self):
        # get block
        block_list = self.BFS()
        for block in block_list:
            for node_id in range(1, len(block)):
                if block[node_id].count < block[node_id - 1].count:
                    return False

        return True

    def get_block_index(self, levels, current_node):
        for index, level in enumerate(levels):
            for node in level:
                if node == current_node:
                    return index

        return -1

    # def get_block_up(self, current_node):
    #     thislevel = [self.root]
    #
    #     while thislevel:
    #         if current_node in thislevel:
    #             return thislevel
    #
    #         nextlevel = list()
    #         for n in thislevel:
    #             if n.left is not None: nextlevel.append(n.left)
    #             if n.right is not None: nextlevel.append(n.right)
    #
    #         thislevel = nextlevel
    #
    #     return thislevel

    def BFS(self):
        levels = []
        thislevel = [self.root]

        while thislevel:
            nextlevel = list()
            for n in thislevel:
                if n.left is not None: nextlevel.append(n.left)
                if n.right is not None: nextlevel.append(n.right)

            levels.append(thislevel)
            thislevel = nextlevel

        return levels
