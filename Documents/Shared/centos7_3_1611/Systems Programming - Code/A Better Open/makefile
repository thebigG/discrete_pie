TARGET = net_io
OBJECTS = libnetfiles.o net_io.o
FLAGS = -Wall -fsanitize=address -g

$(TARGET): libnetfiles.o net_io.o
		gcc $(FLAGS) -o $@ $^


clean:
	rm -f $(TARGET) $(OBJECTS)

%.o: %.c
	gcc $(FLAGS) -c $<

libnetfiles.o: libnetfiles.h
 net_io.o:  libnetfiles.h
