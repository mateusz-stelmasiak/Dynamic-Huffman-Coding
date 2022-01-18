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
            code = self.get_code_from_letter(letter)
            self.update()
            return code

        # add new letter if not found
        node = self.add_new_letter(letter)
        self.update()
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

    def update_node_zero(self, levels):
        for level in levels:
            for node in level:
                if node.letter is None and node.count == 0:
                    self.zeroNode = node
                    break

    def update(self):
        levels = self.BFS()

        while not self.is_sibling_satisfied(levels):
            breaker, breaker_lvl = self.get_node_breaking_sibling_property(levels)
            if breaker is None:
                break;
            print("BEFORE INCOMPLETE SWITCH")
            self.display()

            # check all levels below
            break_flag = False
            for level_id in range(0, breaker_lvl):
                for node_id in range(0, len(levels[level_id])):
                    if levels[level_id][node_id].letter is not None and levels[level_id][node_id].count <= breaker.count - 1:
                        self.switch_nodes(levels[level_id][node_id], breaker)
                        break_flag = True
                        # break
                if break_flag: break

            # siblings check
            if not break_flag:
                node_lvl = levels[breaker_lvl]
                for node_id in range(1, len(node_lvl)):
                    if node_lvl[node_id].count < node_lvl[node_id - 1].count:
                        self.switch_nodes(node_lvl[node_id - 1], node_lvl[node_id])
                        break

            self.recalculate_counts()
            levels = self.BFS()
            print("AFTER INCOMPLETE SWITCH")
            self.display()
            print("")

        breaker, breaker_lvl = self.get_node_breaking_sibling_property(levels)
        if breaker is not None:
            break_flag = False
            for level_id in range(0, breaker_lvl):
                for node_id in range(0, len(levels[level_id])):
                    if levels[level_id][node_id].letter is not None and levels[level_id][
                        node_id].count < breaker.count - 1:
                        self.switch_nodes(levels[level_id][node_id], breaker)
                        break_flag = True
                        # break
                if break_flag: break


        print("AFTER COMPLETE SWITCH")
        self.display()
        self.update_node_zero(levels)

    #
    def is_sibling_satisfied(self, levels):
        # siblings check
        for level in levels:
            for node_id in range(1, len(level)):
                if level[node_id].count < level[node_id - 1].count:
                    return False
        return True


    def get_node_breaking_sibling_property(self, levels):
        for level_index in range(len(levels) - 1, 0, -1):
            for node in levels[level_index]:
                tmp = self.get_node_breaking_sibling_property_aux(node, level_index - 1, levels)
                if tmp is not None:
                    return tmp, level_index - 1

        return None, None

    def get_node_breaking_sibling_property_aux(self, node, level_index, levels):
        # # check all levels above inserted
        # for level_id in range(0, level_index):
        #     for node_id in range(0, len(levels[level_id])):
        #         if levels[level_id][node_id].letter is not None and levels[level_id][node_id].count == node.count - 1:
        #             return levels[level_id][node_id]

        # siblings check
        node_lvl = levels[level_index]
        for node_id in range(1, len(node_lvl)):
            if node_lvl[node_id].count < node_lvl[node_id - 1].count:
                return node_lvl[node_id - 1]

        return None

    def check_node_sibling_property(self, node, node_level, levels):
        node_count = node.count

        # check all levels above inserted
        for level_id in range(0, node_level):
            for node_id in range(0, len(levels[level_id])):
                if levels[level_id][node_id].letter is not None and levels[level_id][node_id].count < node_count - 1:
                    return False

        # siblings check
        node_lvl = levels[node_level]
        for node_id in range(1, len(node_lvl)):
            if node_lvl[node_id].count < node_lvl[node_id - 1].count:
                return False

        return True

    def get_node_level_index(self, node, levels):
        for level_index, curr_level in enumerate(levels):
            for curr_node in curr_level:
                if node == curr_node:
                    return level_index

        return None

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
