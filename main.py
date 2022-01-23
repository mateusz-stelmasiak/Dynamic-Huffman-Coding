from HuffmanClient import *
import time

print("-------------coding-----------------")
# -------------coding-----------------
start_time = time.time()
coder = HuffmanClient()

filename="./texts/smallText"

with open(filename+".txt", encoding='utf-8') as f:
    text = f.read()

for l in text:
    coder.encode(l)
coder.display()
with open(filename+"Coded-string.txt", 'w') as f:
    f.writelines(coder.sent_bits)

s = coder.sent_bits
i = 0
buffer = bytearray()
while i < len(s):
    buffer.append(int(s[i:i + 8], 2))
    i += 8

# now write your buffer to a file
with open(filename+"Coded-binary.txt", 'bw') as f:
    f.write(buffer)

print("coder was running for : --- %s seconds ---" % (time.time() - start_time))

# -------------decoding-----------------
print("-------------decoding----------------")
with open(filename+"Coded-string.txt", encoding='utf-8') as f:
    text_to_decode = f.read()

start_time = time.time()
decoder = HuffmanClient()
decoder.decode_full(text_to_decode)
decoder.display()

print("decoder was running for : --- %s seconds ---" % (time.time() - start_time))
