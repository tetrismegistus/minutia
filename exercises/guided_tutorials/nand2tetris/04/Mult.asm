// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

    @product
    M=0         // product = 0
    @i
    M=0         // i = 0

(LOOP)
    @R1
    D=M
    @i
    D=M-D
    @STOP
    D;JEQ       // if i = R1: STOP
    @i
    M=M+1
    
    @R0
    D=M
    @product
    M=D+M       // product += R0
    
    @LOOP
    0;JMP       // GOTO LOOP

(STOP)
    @product
    D=M
    @R2
    M=D

(END)
    @END
    0;JMP

