OV = bof1-exercise/bof1 bof2-exercise/bof2
PROGRAMS = $(OV)
CFLAGS += -no-pie -g -m32 -mpreferred-stack-boundary=2 -fno-stack-protector -zexecstack

# Convenience to auto-call mcheck before the first malloc()
#CFLAGS += -lmcheck

all: $(PROGRAMS)
clean:
	rm -f $(PROGRAMS)

