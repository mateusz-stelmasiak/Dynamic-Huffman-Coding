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
        self.received_text = ""
        self.sent_text = ""
        self.sent_bits = ""
        self.huffmanTree = HuffmanTree()
        self.cache = {}  # dict of most used letter codes

    # prints the tree
    def display(self):
        print("ClientId: " + str(self.clientId))
        #display if self.sent_text != "": print("SentText: " + str(self.sent_text))
        #display if self.sent_bits != "": print("SentBits: " + str(self.sent_bits))
        if len(self.sent_bits) != 0: compressionS = len(self.sent_bits) * 100 / (len(self.sent_text) * 8)
        if self.sent_bits != "": print("Compression: " + str(compressionS) + "%")
        #display if self.received_text != "": print("ReceivedText: " + str(self.received_text))
        #display if self.received_bits != "": print("All ReceivedBits: " + str(self.received_bits))
        if len(self.received_bits) != 0: compressionR = len(self.received_bits) * 100 / (len(self.received_text) * 8)
        if self.received_bits != "": print("Compression: " + str(compressionR) + "%")
       #display self.huffmanTree.display()

    def encode(self, letter, decoder=None):
        self.sent_text += letter

        # endcoding letter
        node_zero = self.huffmanTree.get_node_zero_code()
        code = self.huffmanTree.add(letter)

        if code == -1:
            send_code = node_zero + letter_to_binary_string(
                letter)  # Node zero kod + kod nowej litery woj
        else:
            send_code = code

        # TODO clear cache on rebuild
        #display print("Node zero code is: " + str(node_zero))
        #display  print("Encoded '" + str(letter) + "' as: " + send_code)
        self.sent_bits += send_code
        #display self.display()

        # send to decoder
        if decoder:
            decoder.decode(send_code)

        return code

    def is_node_zero(self, code):
        node_zero_code = self.huffmanTree.get_node_zero_code()
        for x in range(len(node_zero_code)):
            if node_zero_code[x] != code[x]:
                return False
        return True


    def decode(self, code):
        #is_ascii = code[0] == "0"  # woj
        #acutal_code = code[1:]
        #display  print("node zero code is: " + self.huffmanTree.get_node_zero_code())
        #display print("Received bits: " + str(code))
        self.received_bits += code
        #woj chagnes
        if self.is_node_zero(code):
            code = code[len(self.huffmanTree.get_node_zero_code())+1:]  #woj

            letter = letter_from_binary_string(code)
            self.huffmanTree.add(letter)
            #display  print("Decodedd '" + str(code) + "' as: " + str(letter))
            self.received_text += letter
            #display self.display()
            return letter


        # TODO see if it's a cache hit
        letter = self.huffmanTree.get_letter_from_code(code)
        self.huffmanTree.add(letter)
        #display  print("Decoded '" + str(code) + "' as: " + str(letter))
        self.received_text += letter

       #display self.display()
        return letter
