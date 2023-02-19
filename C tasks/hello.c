
#include <stdio.h>

int main( void ) {

    int W;
    int H;
    int A;
    
    printf("Enter the width: ");
    scanf("%i", &W);
    
    printf("Enter the height: ");
    scanf("%i", &H);
    
    A = W * H;
    
    printf("The area is: %i", A);

  return 0;
}

