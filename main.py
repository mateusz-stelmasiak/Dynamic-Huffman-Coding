from HuffmanClient import *

coder = HuffmanClient()
decoder = HuffmanClient()

text = "abcaaccaba"

for l in text:
    coder.encode(l, decoder)
