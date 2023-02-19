
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#include "game.h"
#include "playGame.h"
#include "endGame.h"

/*
 * Controls the game logic from start to end
 */

void playGame( Game *game ) {

  char symbols[2] = { 'X','O' };
  // player 'X' plays first
  int player = 0;
  int valid;

  // starting board
  printf("New game starting\n");
  

  //showGameVaryLengths(game);
  showGame( game );
  
  // Your game should be controlled by an outer loop
  // Each pass through the loop is one completed move by a player
  
   
  // Request a move from the next player and check it is valid (an unused square within the board)
  //printf("Player %c: Enter your move as row column values:\n",symbols[player]); // use this to request the player move

  for(int i = 0; i<game->maxTurns; i++){ //Loops for the number of possible turns

	if((game->turns)%2 == 0){ //Identifies who's turn it is
		
		player = 0; //Assigns the player variable with player 0
	}
	else{
	
		player = 1; //Assigns the player variable with player 1
		
	}

	printf("Player %c: Enter your move as row column values:\n",symbols[player]);

	char symbol = symbols[player]; //Assigns symbol with the corresponding symbol to the current player
 	
	valid = makeMove(game,symbol); //Validates if a move is valid

	if(valid == 1){

		game->turns = game->turns + 1; //Increments game turns

		showGame(game); //Shows the game board

		if(winGame(game, symbols[player]) == 1){ //Checks to see if a player has won the game (Functionality in endGame.c)
			
			printf("Player %c has won\n",symbols[player]); //Alerts the user a player haas won
			exit(0); //Exits the program as the game is finished
		}
		else if(winGame(game, symbols[player]) == -1){ //Checks to see if the game has drawn
			
			printf("Match is drawn\n"); //Alerts the user the match is a draw
			exit(0); //Exits the program as the game is finished
	
		}
		else{

		}
		
	}
	else{
		
		while(valid == 0){ //Loops until the user enters a correct input
		
			printf("Move rejected. Please try again\n"); //Alerts the user an input was invalid
			valid = makeMove(game,symbols[player]); //Checks the move is valid		

		}

		showGame(game); //Shows the game board	
		game->turns = game->turns + 1; //Increments the turn when the player has eventually entered a correct move
	}


  }

  //valid = makeMove(game, symbols[player]);

  // If the move is invalid you should repeat the request for the current player
  //printf("Move rejected. Please try again\n"); // use this message if move cannot be made. You must repeat the request for a move

  // If the move is valid update the board
  
  // After each completed move display the board 
  //showGame( game );

  // After each valid move you can test for win or draw using functions you implement in endGame.c
  //printf("Player %c has won\n",symbols[player]); // use to announce a winner - game is over
  //printf("Match is drawn\n"); // use to announce a draw - game is over
 
  return;
}

/*
 * Display the game board - do not adjust the formatting
 */

void showGame( Game *game ) {

  printf("\n");
  printf("      0  1  2\n");
  printf("\n");
  printf(" 0    %c  %c  %c\n",game->board[0][0],game->board[0][1],game->board[0][2]);
  printf(" 1    %c  %c  %c\n",game->board[1][0],game->board[1][1],game->board[1][2]);
  printf(" 2    %c  %c  %c\n",game->board[2][0],game->board[2][1],game->board[2][2]);
  printf("\n");

  return;
}


/*
 * Read in the players chosen location
 * Check that the input is a valid empty square
 * If valid then update the board (return 1)
 * If invalid reject the move (return 0)
 */

int makeMove( Game *game, char symbol ) {


  // read the players move from the keyboard, expected as two integers coordinates as shown on the board 

  char coordinates[100];

  fgets(coordinates,100,stdin);

  int coordinate1 = -1; //Sets the initial coordinate to 0 (so if it stays like that we know the input is invalid)

  int coordinate2 = -1; //Sets the initial coordinate to 0 (so if it stays like that we know the input is invalid)

  int numberCount = 0; //Sets the count to count the amount of numbers in the input to 0

  int stringLength = strlen(coordinates); //Gets the length of the input

  for(int i = 0; i<stringLength; i++){ //Loops for the length of the input

	if(isdigit(coordinates[i])){ //Checks to see if the character at i is an integer

		if(numberCount == 0){ //Checks to see if this is the first ordinate

			coordinate1 = atoi(&coordinates[i]); //Sets coordinate1 to the integer value of the first ordinate
			numberCount = numberCount + 1;
		}
		else if(numberCount == 1){ //Checks to see if this is the second ordinate

			
			coordinate2 = atoi(&coordinates[i]); //Sets coordinate2 to the integer value of the second ordinate
			numberCount = numberCount + 1;
			
		}
		else{
			
			return(0); //Returns 0 (Invalid input) as there has been more than ordinates counted in the input

		}

	
	}


  }

  if(coordinate1 != -1){ //Checks to see coordinate1 has changed 

	if(coordinate2 != -1){ //Checks to see coordinate2 has changed

		if(coordinate1<game->boardSize){ //Checks to see coordinate1 is not out of bounds of the game
				
			if(coordinate2<game->boardSize){ //Checks to see coordinate2 is nout out of bounds of the game

  				if(game->board[coordinate1][coordinate2] == '.'){ //Checks to see if the position at the coordinates is empty/not assigned X or O
	
					game->board[coordinate1][coordinate2] = symbol; //Changes the value to the corresponding player symbol
					return(1); //Returns 1 to specify the move is valid
  				}
				else{

					return(0);
				}	
			}
			else{

				return(0);

			}
		}

		else{

			return(0);

		}
	}
	else{

		return(0);
	}
  }
  else{

	return(0);
  }



  // test that the chosen location is a valid empty space

  // if we do not accept the move return 0

  // if we accept then update the board and return 1
	
  //return(1); // move accepted
}


