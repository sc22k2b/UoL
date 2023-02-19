
#include <stdio.h>
#include <stdlib.h>

#include "game.h"
#include "initGame.h"

/*
 * Intialise game data for a new game
 */

Game *initGame( int boardSize, int winLength ) {

  //Game *game;

  // for incorrect boardSize or winLength you should return a NULL pointer

  if(boardSize<3){ //Checks to see board size isn't too small
	
	printf("Incorrect parameter values for board size or win length. Exiting\n");
	return(NULL);
  }
  else if(boardSize>8){ //Checks to see board size isn't too large
	
	printf("Incorrect parameter values for board size or win length. Exiting\n");	
	return(NULL);
  }
  else if(winLength<2){ //Checks to see win length isn't too small

	printf("Incorrect parameter values for board size or win length. Exiting\n");
	return(NULL);
  }
  else if(winLength>boardSize){ //Checks to see board size doesn't exceed the size of the board as this would be too large

	printf("Incorrect parameter values for board size or win length. Exiting\n");
	return(NULL);
  }


  //printf("Incorrect parameter values for board size or win length. Exiting\n");

  // allocate the Game data structure
  // intialise the Game data structure values 
  // board values should be set to '.' (unused location)

	Game *game = (Game *)malloc( sizeof(Game) );

	game->boardSize = 3; //Assigns the board size value
	game->winLength = 3; //Assigns the win length value
	game->maxTurns = (boardSize*boardSize); //Assigns the max turn value (Size of the board squared)
	game->turns = 0; //Initliazes turns to be 0

	for(int i = 0; i<boardSize; i++){ //Loops for the length of the rows
		
		for(int k = 0; k<boardSize; k++){ //Loops for the lenght of the columns

			game->board[i][k] = '.'; //Assigns the . value to every position on the board
		}
	}
  
  return game; //Returns all assigned values
}


