DIR := ../C/
FLAGS := -shared -fPIC -o

main: keyEvents.o health.o gamePlaying.o errorWindow.o
	gcc keyEvents.o health.o gamePlaying.o errorWindow.o $(FLAGS) cFunctions.so
	mingw32-make clean

keyEvents.o:
	gcc -c $(DIR)keyEvents.c

health.o:
	gcc -c $(DIR)health.c

gamePlaying.o:
	gcc -c $(DIR)gamePlaying.c

errorWindow.o:
	gcc -c $(DIR)Error/errorWindow.c

clean:
	del -f *.o