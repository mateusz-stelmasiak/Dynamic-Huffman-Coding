from HuffmanTree import *
from random import randrange


# Something something coder decoder
class HuffmanClient:
    clientId = randrange(1000)
    huffmanTree = HuffmanTree()
    cache = {}  # dict of most used letter codes

    # prints the tree
    def display(self):
        print("ClientId: " + str(self.clientId))
        print("DictSize: " + str(self.huffmanTree.dict_size()))
        self.huffmanTree.display()

    def encode(self, letter, decoder):
        # endcoding letter
        result = self.huffmanTree.add(letter)
        #TODO clear cache on rebuild
        print("Encoded '" + str(letter) + "' as: " + result)

        #send to decoder

        return result

    # def decode(self,code):
    #     #see if it's a cache hit
    #     # self.huffmanTree
    #
    #     #return letter
