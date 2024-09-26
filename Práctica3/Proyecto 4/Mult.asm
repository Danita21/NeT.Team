// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

@R2
M=0          // Initialize R2 to 0

@R0
D=M          // Load R0 into D
@END
D;JEQ        // If R0 == 0, jump to END

@R1
D=M          // Load R1 into D
@END
D;JEQ        // If R1 == 0, jump to END

@R0
D=M          // Load R0 into D
@R3
M=D          // Set R3 = R0 (counter)

(LOOP)
@R1
D=M          // Load R1 into D
@R2
M=D+M        // Add R1 to R2 (R2 = R2 + R1)

@R3
M=M-1        // Decrement R3
D=M
@LOOP
D;JGT        // If R3 > 0, repeat loop

(END)
@R2
M=0          // Initialize R2 to 0

@R0
D=M          // Load R0 into D
@END
D;JEQ        // If R0 == 0, jump to END

@R1
D=M          // Load R1 into D
@END
D;JEQ        // If R1 == 0, jump to END

@R0
D=M          // Load R0 into D
@R3
M=D          // Set R3 = R0 (counter)

(LOOP)
@R1
D=M          // Load R1 into D
@R2
M=D+M        // Add R1 to R2 (R2 = R2 + R1)

@R3
M=M-1        // Decrement R3
D=M
@LOOP
D;JGT        // If R3 > 0, repeat loop

(END)
