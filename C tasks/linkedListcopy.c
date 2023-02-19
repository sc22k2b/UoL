
#include <stdio.h>
#include <stdlib.h>

/*
 * structures
 */

typedef struct bankAccount{

	int bankNumber;
	float balance;
	char gender;

} Bank;

typedef struct nodeData {
  int intData;
  float floatData;
} Data;

typedef struct node {
  Data *data;
  struct node *next;
} Node;

/*
 * function headers
 */

void assign_data(Bank *bank_array);

/*
 * main
 */

int main( void ) {

	Bank bank_array[5];
	assign_data(bank_array);
  
}

void assign_data(Bank *bank_array){

	bank_array[0].bankNumber = 1;
	bank_array[0].balance = 11.22;
	bank_array[0].gender = 'm';

	for(int i = 0; i<5; i++){

		printf("%i \n",bank_array[0].bankNumber);
		printf("%f \n",bank_array[0].balance);
		printf("%c \n", bank_array[0].gender);

	}
}


