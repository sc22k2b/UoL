
#include <stdio.h>
#include <math.h>

int main( void ) {

  int number;
  int factorial = 1;

  printf("Enter the number: ");
  scanf("%i", &number);
  
  for(int i = 0; i<number; i++){
    
    factorial = factorial * (number - i);
   }

  printf("Factorial is: %i", factorial);
  


  return 0;
}

