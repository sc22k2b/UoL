//Set up a count
@4
D=M
@shiftCount
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
@3
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
@3
M=D&M


(skipRotate)
//Shift left 1 place
@3
D=M
M=D+M

@additional
D=M
M=0
@3
M=D+M


//Check 

//Increment and add 1 if the msb was in there and the count >1 1
@shiftCount
M=M-1
D=M
@shift
D;JGT

@3
D=M
@5
M=D


//Ends the function
(end)
@end
0;JMP


