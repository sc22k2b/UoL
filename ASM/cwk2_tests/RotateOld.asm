@65535
D=A
@maxBit
M=D

@4
D=M
@count
M=D

(multiply)
@3
D=M	//Loads the original number into D
M=M+D	//Doubles it - has the effect of shifting it left 1 place
@count	//Decrements count
M=M-1
D=M

@multiply
D;JGT	//Continues the loop as long as it above 0

@1
D=A
@andVariable
M=D

@4	//Creates the count again so the and variable can be shifted accordingly
D=M
@count
M=D

(multiplyAnd)	//Shifts the and by the same as the original number
@andVariable
D=M	//Loads the original number into D
M=M+D	//Doubles it
@count	//Decrements count
M=M-1
D=M

@multiplyAnd
D;JGT	//Continues the loop as long as it above 0

@16	//The value 16 is the number of times we want to loop (16 bit long number)
D=A	//Place the value 16 in the data register
@count	//Initialise a count location
M=D	//Place the value 16 in the count location

@0	//Get the value 0
D=A	//Put 0 in the data register
@sum	//Set up a new sum memory location
M=D	//Put the value 0 into the sum memory location

(loop)
@andVariable //Ands together the current position bit and the shifted original number
D=M
@3
D=D&M
@andResult
M=D

@maxBit //Checks to see if the number exceeds the max number of bits
D=D-M
@inBounds //Will jump past repositioning if within bounds
D;JLT

//**NEED TO JUMP TO INCREMENT ONCE REPOSITIONED***

@32768	//Maxiumum bit value
D=A
@outOfBoundsAnd
M=D

@16	//Maximum count value
D=A
@maxCount
M=D

@1
D=A
@startingValue	//Retrieves a starting 1 to add to the sum 
M=D

@count
D=M
@maxCount
D=M-D
@countOutOfBounds	//Retrieves the count by taking the difference 
//between the current count and max count
M=D

(outOfBoundsAndChecker)
M=M+D	//Doubles the anding number
@3
D=D&M	//Ands the two things together
@andResultOOB
M=D
@incrementOutOfBounds	//Skips if the and returned a 0 (values didnt match)
D;JLE


(addOnLoop)
@startingValue	//Doubles the 1 for all the remaining counts
D=M
M=D+M

@countOutOfBounds	//Incremenets the count
M=M-1
D=M
@addOnLoop	//Continues to loop if D is above 0	
D;JGT

@startingValue
D=M
@sum
M=D+M	//Adds to the sum the value if the bit were to be rotated


(incrementOutOfBounds)
@outOfBoundsAnd
D=M
M=M+D
@count
M=M-1
D=M
@loop	//Continues the loop as long as the count is above 0
D;JGT

@skipInBounds
0;JMP


//************************************************

(inBounds)
@andResult
D=M
@increment	//Jumps past the summing as the value did not contain what was in the and variable
D;JLE
@andVariable
D=M
@sum
M=D+M

(increment)
@andVariable	//Doubles the and variable (the next bit position)
D=M
M=M+D
@count
M=M-1
D=M
@loop	//Continues the loop as long as the count is above 0
D;JGT

(skipInBounds)
@sum	//Places the final value into RAM[5]
D=M
@5
M=D

(end)	//Ends the function
@end
0;JMP





