//**************SETUP*********************
//Set up a count
@4	//4 rounds of encryption
D=A
@count
M=D

//Set up a mask
@255
D=A
@leftMask
M=D

//Extract left 8 bits (Possible rotate to treat it like an 8 bit number)
//Rotate the 16 bit plaintext to have the first 8 bits become the last 8 bits
//Mask of the last 8 bits (&0000000011111111)

//#################Rotate the plaintext 8 places########

//Set up a count
@8
D=A
@shiftCount
M=D

@2
D=M
@plaintextRotated
M=D

@16384
D=A
D=D+A
@bigBit
M=D

@32767
D=A
@removeMSB
M=D


//Shift the values and check for the maximum bit being occupied - rotate it if there is remaining count
(shift)
//Rotate

//Mask the Msb off
@bigBit
D=M
@plaintextRotated
D=D&M
@msb	//Store the msb (0 or 32768)
M=D

@msb
D=M
@skipRotate	//Skip rotate as the last shift did not contain the msb
D;JEQ

@1	//Store a 1 to be added on after the next shift
D=A
@additional
M=D

@removeMSB	//Remove the msb from the number to stop it overflowing
D=M
@plaintextRotated
M=D&M


(skipRotate)
//Shift left 1 place
@plaintextRotated
D=M
M=D+M

@additional
D=M
M=0
@plaintextRotated
M=D+M

//Check 

//Increment and add 1 if the msb was in there and the count >1 1
@shiftCount
M=M-1
D=M
@shift
D;JGT


//######################################################

//Mask off the last 8 bits (first 8 bits before rotating)

@leftMask
D=M
@plaintextRotated
D=D&M	//Mask off the last 8 bits
@leftBits
M=D


//Extract right 8 bits
//Mask off last 8 bits (&0000000011111111)

@2
D=M
@leftMask
D=D&M	//Mask off the last 8 bits in the original plaintext
@rightBits
M=D

//****************************************

//**************Switch and function*******
//Loop to switch the bits round
(loop)

//Function on R

@1	//Negate the key for the function: A XOR ¬B
D=M
@negatedKey
M=!D

@leftMask	//Retain 8 bit key length by masking off any additional bits
D=M
@negatedKey
M=D&M

//######################XOR - Function########################

//NAND
@rightBits
D=M
@negatedKey
D=D&M

@nandResult
M=!D

@leftMask	//Retain an 8 bit length (mask off bits 9-16)
D=M
@nandResult
M=D&M

//OR
@rightBits
D=M
@negatedKey
D=D|M

@orResult
M=D

//AND
@nandResult
D=M
@orResult
D=D&M

@functionResult
M=D

//######################################################

//######################XOR - Cipher####################

//NAND
@leftBits
D=M
@functionResult
D=D&M

@nandResult
M=!D

@leftMask	//Retain an 8 bit length (mask off bits 9-16)
D=M
@nandResult
M=D&M

//OR
@leftBits
D=M
@functionResult
D=D|M

@orResult
M=D

//AND
@nandResult
D=M
@orResult
D=D&M

@functionXOR
M=D

//#############################################################



//Rotate key for next use

@128	//Set up the msb for an 8 bit value
D=A
@eighthBit
M=D

//Mask off the most signifcant bit so it isn't lost when rotating
@1	//The key
D=M
@eightBit
D=D&M

@skipRotate2	//Dont add an additional 1 to the shift as the key did not contain the msb
D;JEQ

@1
D=A
@rotatedBit
M=D


(skipRotate2)
@1
D=M
M=D+M

@rotatedBit	//Add the additional bit that rotated round
D=M
M=0
@1
M=D+M

//Switch the bit positions (left bits -> right bits & right bits -> left bits)

@rightBits
D=M
@nextLeftBits
M=D

@functionXOR
D=M
@nextRightBits
M=D

@nextLeftBits	//Switch right bits to left bits
D=M
@leftBits
M=D

@nextRightBits		//Switch left bits to right bits
D=M
@rightBits
M=D


//Increment
@count	//Continues the loop whilst the count (4) is above 0
M=M-1
D=M
@loop
D;JGT



//******************************************

//*****************Place result in RAM******

//Shift left bits up 8 places again to make a 16 bit number (Reverse the initial right shift/left rotate)

@8
D=A
@reverseCount
M=D

(shiftEight)
@leftBits	//Shift the bits left 1 place
D=M
M=D+M

@reverseCount
M=M-1
D=M
@shiftEight
D;JGT

@leftBits
D=M
@rightBits
D=D+M
@0
M=D


//*******************************************

//***********************END*****************

(end)
@end
0;JMP

//********************************************