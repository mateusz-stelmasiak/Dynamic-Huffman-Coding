from HuffmanClient import *
import time

# coder = HuffmanClient()
#
# with open("beemovie.txt", encoding='utf-8') as f:
#     text = f.read()
#
# for l in text:
#     coder.encode(l)
# coder.display()

start_time = time.time()
decoder = HuffmanClient()
decoder.decode_full("01000001001000010010")
decoder.display()


print("program was running for : --- %s seconds ---" % (time.time() - start_time))
