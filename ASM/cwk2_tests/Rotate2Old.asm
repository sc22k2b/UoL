//Calculates the maximum the value can be shifted before overflowing
@15 //CB 16
D=A
@4
D=D-M
@maxShift
M=D

//Sets up a count
@maxShift
D=M
@count
M=D

//Sets up a sum
@0
D=A
@sum
M=D

//Sets up andVariable to hold the value that will be used to extract each bit
@1
D=A
@andVariable
M=D

(loop)
//Extracts the bit for the specific and
@andVariable
D=M
@3
D=D&M
@andResult
M=D

//Jumps to increment if it does not contain a certain bit so no summing needed
@increment
D;JLE

@4
D=M
@shiftCount
M=D

(shift)	//Shifts the bit the number of places specified
@andResult
D=M
M=D+M

@shiftCount	//Decrements the shift count
M=M-1
D=M

@shift
D;JGT

@andResult
D=M
@sum
M=D+M

(increment)	//Doubles the and variable and decrements the count
@andVariable
D=M
M=M+D
@count
M=M-1
D=M
@loop	//Continues the loop whilst count is above 0
D;JGT

//***** ROTATION **********

//Resets the bit so that the bits that cant be shifted will be rotated
@1
D=A
@rotateBit
M=D

//Sets up a count to count through the remaining bits that have to be rotated
@15 //CB 16
D=A
@maxShift
D=D-M
@remainingCount
M=D

(rotate)
@andVariable
D=M
@3
D=D&M
@andResult
M=D

@incrementRotate	//Skips over the summation as the number did not contain the bit
D;JLE

//Adds the rotated bit to the sum

//Calculates the remaining number of bits the bit needs to be shifted
//@16
//D=A
//@maxShift
//D=D-M
//@remainingShift
//M=D

//(rotateShift)
//@andResult
//D=M
//M=D+M

//@remainingShift	//Decrements the shift count
//M=M-1
//D=M

//@rotateShift
//D;JGT


@rotateBit
D=M
@sum
M=D+M

(incrementRotate)
@andVariable
D=M
M=M+D

@remainingCount
M=M-1
D=M

@rotateBit
D=M
M=D+M

@remainingCount
D=M

@rotate	//Continues the loop whilst count is above 0
D;JGT

//Places the final value into RAM[5]
@sum
D=M
@5
M=D

//Ends the function
(end)
@end
0;JMP


