from HuffmanTree import *
from random import randrange


# return a string binary representation
# of ASCII code for given letter
def letter_to_binary_string(letter):
    return ''.join([bin(ord(x))[2:].zfill(8) for x in letter])


def letter_from_binary_string(b_string):
    return chr(int(b_string, 2))


# Something something coder decoder
class HuffmanClient:
    def __init__(self):
        self.clientId = randrange(1000)
        self.received_bits = ""
        self.received_bits_readable = ""  # ASCII characters replaced with [CHAR]
        self.received_text = ""
        self.sent_text = ""
        self.sent_bits = ""
        self.sent_bits_readable = ""  # ASCII characters replaced with [CHAR]
        self.huffmanTree = HuffmanTree()
        self.cache = {}  # dict of most used letter codes

    # prints the tree
    def display(self):
        print("ClientId: " + str(self.clientId))
        if self.sent_text != "": print("SentText: " + str(self.sent_text))
        if self.sent_bits != "": print("SentBits: " + str(self.sent_bits))
        if len(self.sent_bits) != 0: compressionS = len(self.sent_bits) * 100 / (len(self.sent_text) * 8)
        if self.sent_bits_readable != "": print("Sent: " + str(self.sent_bits_readable))
        if self.sent_bits != "": print("starting was : " + str(len(self.sent_text) * 8) + "bits")
        if self.sent_bits != "": print("Sent total of : " + str(len(self.sent_bits)) + "bits")
        if self.sent_bits != "": print("Compression: " + str(compressionS) + "%")

        if self.received_text != "": print("ReceivedText: " + str(self.received_text))
        if self.received_bits != "": print("All ReceivedBits: " + str(self.received_bits))
        if self.received_bits_readable != "": print("Received: " + str(self.received_bits_readable))
        if len(self.received_bits) != 0: compressionR = len(self.received_bits) * 100 / (len(self.received_text) * 8)
        if self.received_bits != "": print("Compression: " + str(compressionR) + "%")
        self.huffmanTree.display()

    # encodes a single letter
    def encode(self, letter):
        self.sent_text += letter

        # find node zero
        node_zero = self.huffmanTree.get_node_zero_code()
        code = self.huffmanTree.add(letter)

        # code -1 if new letter was added
        if code == -1:
            letter_binary = letter_to_binary_string(letter)
            # check for polish chars
            if len(letter_binary) > 8:
                letter_binary = "1" + letter_binary  # if polish encode with prefix 1
            else:
                letter_binary = "0" + letter_binary

            send_code = node_zero + letter_binary  # Node zero code + new letter code
            self.sent_bits_readable += node_zero + "[" + letter + "]"
        else:
            send_code = code
            self.sent_bits_readable += code

        self.sent_bits += send_code

    def is_node_zero(self, code):
        node_zero_code = self.huffmanTree.get_node_zero_code()

        for x in range(len(node_zero_code)):
            if node_zero_code[x] != code[x]:
                return False

        return True

    def decode_full(self, code):
        buffer = ""
        bit_index = 0

        # first 8 bits are always a letter
        # check for polish chars
        polish_char_prefix = code[0]
        offset = 9
        if polish_char_prefix == "1":
            offset = 10
        first_letter = code[1:offset]
        letter = letter_from_binary_string(first_letter)
        self.huffmanTree.add(letter)
        self.received_text += letter
        # cut off 8 first bits form code
        code = code[offset:]

        while True:
            # try to find a node that has the path given in buffer
            curr_node = self.huffmanTree.get_node_from_code(buffer)

            # if not found, load next bit into the buffer
            if curr_node is None:
                if bit_index < len(code): buffer = buffer + code[bit_index]
                bit_index += 1
            # found zero node, add new letter
            elif curr_node.count == 0:
                # check for polish chars
                polish_char_prefix = code[bit_index]
                offset = 9
                if polish_char_prefix == "1":
                    offset = 10

                letter_binary = code[bit_index+1:bit_index + offset]
                letter = letter_from_binary_string(letter_binary)
                self.huffmanTree.add(letter)
                self.received_text += letter
                # skip 8 chars (ASCII enconding)
                bit_index += offset+1
                buffer = ""
            # found normal letter, increment
            else:
                letter = self.huffmanTree.get_letter_from_code(buffer)
                self.huffmanTree.add(letter)
                self.received_text += letter
                buffer = ""

            # exit while if all bits have been interpreted
            if bit_index > len(code):
                break

    def decode(self, code):
        self.received_bits += code

        # woj chagnes
        if self.is_node_zero(code):
            code = code[len(self.huffmanTree.get_node_zero_code()) + 1:]  # woj

            letter = letter_from_binary_string(code)
            self.huffmanTree.add(letter)
            # display  print("Decodedd '" + str(code) + "' as: " + str(letter))
            self.received_text += letter
            # display self.display()
            return letter

        letter = self.huffmanTree.get_letter_from_code(code)
        self.huffmanTree.add(letter)
        # display  print("Decoded '" + str(code) + "' as: " + str(letter))
        self.received_text += letter

        # display self.display()
        return letter
