
#include <stdio.h>

#include "game.h"
#include "endGame.h"

/*
 * Functions in this module check for wins and draws
 */

// test all possible ways the game can be won for one player
int winGame( Game *game, char symbol ) {

  // return 1(true) if game is won, 0(false) otherwise
  //
  // You may wish to define further functions to test different win conditions
  // Games can be won with horizontal, vertical or diagonal lines

  if(downWin(game) == 1){ //Checks to see if the player has won with a downwards collection of the same symbol

	return(1);

  }
  else if(acrossWin(game) == 1){ //Checks to see if the player has won with an across collection of the same symbol

	return(1);

  }
  else if(diagonalWinLeft(game) == 1){ //Checks to see if the player has won with a diagonal collection of the same symbol going left to right

	return(1);

  }
  else if(diagonalWinRight(game) == 1){ //Checks to see if the player has won with a diagonal collection of the same symbol going right to left

	return(1);

  }
  else if(drawGame(game) == 1){ //Checks to see if the match has resulted in a draw

	return(-1);

  }
  else{

	return(0); //Returns 0 as the match has not been won or drawn and therefore can continue
  }

  //return 0;  // continue
}

// test for a draw
int drawGame( Game *game ) {

  // return 1(true) if game is drawn, 0(false) otherwise

  if(game->maxTurns == game->turns){ //Checks to see if the max number of turns has been reached as this is neccesary for a draw

	if(downWin(game) == 0){ //Checks to see there isn't a win on the board
		
		if(acrossWin(game) == 0){ //Checks to see there isn't a win on the board

			if(diagonalWinLeft(game) == 0){ //Checks to see there isn't a win on the board

				if(diagonalWinRight(game) == 0){ //Checks to see there isn't a win on the board

					return(1);

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

  //return 0; // continue
}

int downWin(Game *game){

	int gameWon = 0;
	int count = 0;

	for(int i = 0; i<game->boardSize; i++){ //Loops for the number of rows

		for(int k = 0; k<game->boardSize; k++){ //Loops for the number of columns (-1)

			if(game->board[k][i] != '.'){ //Checks to see the value at k,i on the board is an actual symbol

				if(k<game->boardSize-1){ //Stops the loop for stepping outside of the array
					
					if(game->board[k][i] == game->board[k+1][i]){ //Compares if the symbol is the same as the symbol below it
				
						gameWon = 1; //Identifies that the game could win (if potentially more matches are made)
						count = count + 1; //Increments the count

						if(game->winLength == (count+1)){ //Checks to see if the succesive symbols has reached the win length
							
							break; //Breaks out the loop as the game has been won
	
						}

					}
					else{
						
						//Resets all values as there has been an incorrect value found and therefore the game has not been won
						gameWon = 0;
						count = 0;
						break;
					}
				}
				else{
					//Resets all values as there has been an incorrect value found and therefore the game has not been won
					gameWon = 0;
					count = 0;
					break;
				
				}
			}
			else{
				//Resets all values as there has been an incorrect value found and therefore the game has not been won
				gameWon = 0;
				count = 0;
			}

		}
		if(gameWon == 1){
			
			break;

		}

	}

	return(gameWon);

}

int acrossWin(Game *game){

	int gameWon = 0;
	int count = 0;

	for (int i = 0; i<game->boardSize; i++){ //Loops for the number of rows

		for(int k = 0; k<game->boardSize; k++){ //Loops for the number of columns

			if(game->board[i][k] != '.'){ //Checks to see if the value is an actual used position on the board
				
				if(k<game->boardSize-1){ //Stops the program from overstepping out the array

					if(game->board[i][k] == game->board[i][k+1]){ //Compares the symbol with the symbol adjacent to it

						gameWon = 1; //Sets game won as there is a potential win in the game
						count = count + 1; //Increments the count
		
						if(game->winLength == (count+1)){ //Checks to see if the win length has been reached
	
							break; //Breaks from the loop as the win length has been reached so there is no need to keep looking for matching values
						}

					}
					else{
						//Resets all values as there has been an incorrect value found and therefore the game has not been won
						gameWon = 0;
						count = 0;
						break;
				
					}
				}
				else{
					//Resets all values as there has been an incorrect value found and therefore the game has not been won
					gameWon = 0;
					count = 0;
					break;
				}
					
			}
			else{
				//Resets all values as there has been an incorrect value found and therefore the game has not been won
				gameWon = 0;
				count = 0;

			}

		}

		
		if(gameWon == 1){
			
			break;
		}
	}

	return(gameWon);

}

int diagonalWinLeft(Game *game){

	int gameWon = 0;
	int count = 0;
	int row = 0;

	for(int i = 0; i<game->boardSize; i++){ //Loops for the number of rows

		row = i; //Retrieves the row currenlty in use

		for(int k = 0; k<game->boardSize; k++){ //Loops for the number of columns

			if(game->board[row][k] != '.'){ //`Checks to see the position on the board has been played on

				if(row<game->boardSize-1){ //Stops the progra from steppping outside the array

					if(k<game->boardSize-1){ //Stops the progra from steppping outside the array	

						if(game->board[row][k] == game->board[row+1][k+1]){ //Comapares the symbol at the index with the one diagonal (left) to it

							gameWon = 1; //Sets game won as there is a potential that the game has been won
							count = count + 1; //Increments the count
							row++; //Increments the row number

							if(game->winLength == (count+1)){ //Checks to see if the win length has been reached
						
								
								break; //Breaks as the win length has been reached so there is no need to keep looking
							}
						}
						else{
							//Resets all values as there has been an incorrect value found and therefore the game has not been won
							gameWon = 0;
							count = 0;
							break;
						}
					}
					else{
						//Resets all values as there has been an incorrect value found and therefore the game has not been won
						gameWon = 0;
						count = 0;
						break;
					}
				}
				else{
					//Resets all values as there has been an incorrect value found and therefore the game has not been won
					gameWon = 0;
					count = 0;
					break;
				}
					
			}
			else{
				//Resets all values as there has been an incorrect value found and therefore the game has not been won
				gameWon = 0;
				count = 0;
			}


		}

		if(gameWon == 1){
			
			break;
		
		}


	}

	return(gameWon);

}

int diagonalWinRight(Game *game){

	int gameWon = 0;
	int count = 0;
	int row = 0;
	int column = 0;

	for(int i = 0; i<game->boardSize; i++){ //Loops for the number of rows

		row = i; //Retrieves the row currently being looked at

		for(int k = 0; k<game->boardSize; k++){ //Loops for the number of columns

			column = game->boardSize-(k+1); //Retreives the column currently being looked at

			if(game->board[row][column] != '.'){ //Checks to see the position on the board has actually been played on (And therefore worth checking)

				if((game->boardSize)-1>row){ //Stops the program from stepping outside the array
					
					if(column>0){ //Stops the program from stepping outside the array
							
						if(game->board[row][column] == game->board[row+1][column-1]){ //Compares the symbol at the index with symbol diagonal (right) to it

							gameWon = 1; //Sets game won as there is potentially a game winning streak
							count = count + 1; //Increments count
							row++; //Increments the next row to be looked at
							column--; //Decrements the next column to be looked at


							if(game->winLength == (count+1)){ //Checks to see if the win length has been reached
						
								break; //Breaks as there is no need to keep looking
							}
						}
						else{
							//Resets all values as there has been an incorrect value found and therefore the game has not been won
							gameWon = 0;
							count = 0;
							break;
						}
					}
					else{
						//Resets all values as there has been an incorrect value found and therefore the game has not been won
						gameWon = 0;
						count = 0;
						break;
					}
				}
				else{
					//Resets all values as there has been an incorrect value found and therefore the game has not been won
					gameWon = 0;
					count = 0;
					break;
	
				}
					
			}
			else{
				//Resets all values as there has been an incorrect value found and therefore the game has not been won
				gameWon = 0;
				count = 0;
			}


		}

		if(gameWon == 1){

			break;
		
		}


	}

	return(gameWon);

}
