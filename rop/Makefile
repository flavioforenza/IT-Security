OV = rop-simple/simple-rop rop-ex1/rop-ex1 rop-secret/rop-vuln
PROGRAMS = $(OV)
CFLAGS += -no-pie -m32 -mpreferred-stack-boundary=2 -fno-stack-protector -zexecstack -g

# Convenience to auto-call mcheck before the first malloc()
#CFLAGS += -lmcheck

all: $(PROGRAMS)
clean:
	rm -f $(PROGRAMS)

