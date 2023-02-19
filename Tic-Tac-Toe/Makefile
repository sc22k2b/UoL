
# code details

EXE = ./bin/tictactoe
SRC = main.c initGame.c playGame.c endGame.c                 # ** list source code here **
OBJ = main.o initGame.o playGame.o endGame.o                 # ** list object code here **

# generic build details

CC     = gcc
CFLAGS = -std=c99 -Wall
CLIBS  = 
CLINK  = 

# compile to object code

%.o: %.c
	$(CC) -c $(CFLAGS) $(CLIBS) $< -o $@

# build executable: type 'make'

$(EXE): $(OBJ)
	$(CC) $(OBJ) $(CLINK) -o $(EXE) 

# clean up and remove object code and executable: type 'make clean'

clean:
	rm -f $(OBJ) $(EXE)

# dependencies

main.o:	main.c	game.h
initGame.o: initGame.c game.h initGame.h
playGame.o: playGame.c game.h playGame.h
endGame.o: endGame.c game.h endGame.h

#
# ** put code dependencies here **
#
