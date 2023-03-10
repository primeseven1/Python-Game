DIR = ../C
FLAGS = -shared -fPIC -O2 -o
C_SRC := $(wildcard $(DIR)/*.c) $(wildcard $(DIR)/**/*.c)
OBJ := $(patsubst %.c, %.o, $(notdir $(C_SRC)))

main: obj
	gcc $(OBJ) $(FLAGS) cFunctions.so
	make clean

obj:
	gcc -c $(C_SRC)

clean:
	del -f *.o
