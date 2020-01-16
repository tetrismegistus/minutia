// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

    @SCREEN
    D=A
    @curr_word
    M=D             //curr_word = SCREEN
    @8192
    D=D+A
    @max_word
    M=D             // max_word = SCREEN + 8191

(FILL)
    @KBD
    D=M
    @SETWHITE
    D;JEQ           // IF KBD = 0 goto SETWHITE
    D=-1            // else D = -1
    @ADDPIX
    0;JMP           // goto ADDPIX
(SETWHITE)
    D=0
(ADDPIX)
    @curr_word
    A=M
    M=D             // M[curr_word]=D
    @1
    D=A
    @curr_word
    M=D+M           // curr_word += 16
    D=M
    @max_word
    D=D-M
    @RESET
    D;JEQ           // if curr_word = max_word; goto RESET
    @END
    0;JMP           // goto END
(RESET)
    @SCREEN
    D=A
    @curr_word
    M=D             // curr_word = SCREEN
(END)
    @FILL
    0;JMP           // goto FILL
