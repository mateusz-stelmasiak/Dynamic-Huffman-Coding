from HuffmanClient import *
import time
print("-------------coding-----------------")
#-------------coding-----------------
start_time = time.time()
coder = HuffmanClient()

with open("beemovie.txt", encoding='utf-8') as f:
    text = f.read()

for l in text:
    coder.encode(l)
coder.display()
with open("beemovieCoded.txt", 'w') as f:
    f.writelines(coder.sent_bits)

print("coder was running for : --- %s seconds ---" % (time.time() - start_time))


#-------------decoding-----------------
print("-------------decoding----------------")
with open("beemovieCoded.txt", encoding='utf-8') as f:
    text_to_decode = f.read()
print("Received data:" + text_to_decode)

start_time = time.time()
decoder = HuffmanClient()
decoder.decode_full(text_to_decode)
decoder.display()

print("decoder was running for : --- %s seconds ---" % (time.time() - start_time))
