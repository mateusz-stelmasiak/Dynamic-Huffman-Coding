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
        self.received_text = ""
        self.sent_text = ""
        self.huffmanTree = HuffmanTree()
        self.cache = {}  # dict of most used letter codes

    # prints the tree
    def display(self):
        print("ClientId: " + str(self.clientId))
        print("SentText: " + str(self.sent_text))
        print("DictSize: " + str(self.received_text))
        print("DictSize: " + str(self.huffmanTree.dict_size()))
        self.huffmanTree.display()

    def encode(self, letter, decoder=None):
        self.sent_text+=letter

        # endcoding letter
        code = self.huffmanTree.add(letter)

        if code == -1:
            send_code = str(0) + letter_to_binary_string(letter)
        else:
            send_code = str(1) + code

        # TODO clear cache on rebuild
        print("Encoded '" + str(letter) + "' as: " + send_code)
        self.display()

        # send to decoder
        if decoder:
            decoder.decode(send_code)

        return code

    def decode(self, code):
        is_ascii = code[0] == "0"
        acutal_code = code[1:]

        if is_ascii:
            letter = letter_from_binary_string(acutal_code)
            self.huffmanTree.add(letter)
            print("Decoded '" + str(code) + "' as: " + str(letter))
            self.display()
            self.received_text += letter
            return letter

        # TODO see if it's a cache hit
        letter = self.huffmanTree.get_letter_from_code(acutal_code)
        self.huffmanTree.add(letter)
        print("Decoded '" + str(code) + "' as: " + str(letter))
        self.display()
        self.received_text += letter
        return letter
