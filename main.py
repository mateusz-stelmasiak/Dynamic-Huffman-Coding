from HuffmanClient import *
import time

coder = HuffmanClient()
decoder = HuffmanClient()
with open("beemovie.txt", encoding='utf-8') as f:
    text = f.read()
start_time = time.time()
for l in text:
    coder.encode(l, decoder)

coder.display()
with open("beemovieCoded.txt", 'w') as f:
    f.writelines(coder.sent_bits)

print("program was running for : --- %s seconds ---" % (time.time() - start_time))
