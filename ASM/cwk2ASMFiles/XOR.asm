//NAND A and B
@3
D=M
@4
D=D&M

@nandResult
M=!D


//OR A and B
@3
D=M
@4
D=D|M

@orResult
M=D

//AND results
@nandResult
D=M
@orResult
D=D&M

//Place the result in RAM[5]
@5
M=D

(end)
@end
0;JMP





