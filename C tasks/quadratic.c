
#include <stdio.h>
#include <math.h>

int main( void ) {

  float square;
  float x;
  float number;

  float root1;
  float root2;

  printf("Enter the coeffecient of x squared ");
  scanf("%f", &square);

  printf("Enter the coeffecint of x ");
  scanf("%f", &x);
 
  printf("Enter the final number ");
  scanf("%f", &number);

  root1 = (-x + sqrt((x*x) - (4*square*number)))/(2*square);
  root2 = (-x - sqrt((x*x) - (4*square*number)))/(2*square);

  printf("Root 1: %f", root1);
  printf("Root 2: %f", root2);


  return 0;
}

