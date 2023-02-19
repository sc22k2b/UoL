
#include <stdio.h>
#include <math.h>

int main( void ) {

  int year;
  printf("Enter the year");
  scanf("%i", &year);

  if(year%400 == 0){
	printf("The year is a leap year");
 }
  else if((year%100 == 0) ){
	printf("The year is not a leap year");
 }
  else if(year%4 == 0){
	printf("The year is a leap year");
 }
  else{
	printf("The year is not a leap year");
 }
  


  return 0;
}

