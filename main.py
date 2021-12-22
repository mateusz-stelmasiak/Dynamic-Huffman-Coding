from HuffmanClient import *

coder = HuffmanClient()
decoder = HuffmanClient()

text = "abcaaac"

for l in text:
    coder.encode(l, decoder)

