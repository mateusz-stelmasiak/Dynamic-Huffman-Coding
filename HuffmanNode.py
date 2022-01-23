max_dict_size = 255


# A single node of the huffman tree
# node of binary tree, holding a letter and its count
class HuffmanNode:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.count = 0
        self.letter = None
        self.rank = (max_dict_size * 2) - 1

    # prints tree starting on node
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    # returns list of strings, width, height, and horizontal coordinate of the root.
    def _display_aux(self):

        # No child.
        if self.right is None and self.left is None:
            line = ""
            if self.letter is not None:
                line = "  " + self.letter + " "
            line = line + str(self.count)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = ""
            if self.letter is not None:
                s = self.letter + " "
            s = s + str(self.count)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = ""
            if self.letter is not None:
                s = self.letter + " "
            s = s + str(self.count)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%d' % self.count
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
