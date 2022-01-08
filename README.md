# Instruction-Code Convertor


Modified on this repo:

https://github.com/souvicksaha95/Opcode-Generator-for-MIPS32-RISC-processor

## 2022/1/4 Update
Now Corresponding to PPT of XJTU CAI 

## Instructions Convert to Codes
Run

    python instr2code.py <filename>  [--print_binary] [--print_hex]

An Example:

    python instr2code.py instructions.txt  --print_binary --print_hex

Results:
    
    ADDI R2 R0 5
    ADDI R3 R0 12
    ADDI R7 R3 65527
    OR R4 R7 R2
    AND R5 R3 R4
    ADD R5 R5 R4
    BEQ R5 R7 10
    SLT R4 R3 R4
    BEQ R4 R0 1
    ADDI R5 R0 0
    SLT R4 R7 R2
    ADD R7 R4 R5
    SUB R7 R7 R2
    SW R7 68 R3
    LW R2 80 R0
    J 11
    ADDI R2 R0 1
    SW R2 84 R0
    
    00100000000000100000000000000101
    00100000000000110000000000001100
    00100000011001111111111111110111
    00000000111000100010000000100101
    00000000011001000010100000100100
    00000000101001000010100000100000
    00010000101001110000000000001010
    00000000011001000010000000101010
    00010000100000000000000000000001
    00100000000001010000000000000000
    00000000111000100010000000101010
    00000000100001010011100000100000
    00000000111000100011100000100010
    10101100011001110000000001000100
    10001100000000100000000001010000
    00001000000000000000000000010001
    00100000000000100000000000000001
    10101100000000100000000001010100
    
    20020005
    2003000c
    2067fff7
    00e22025
    00642824
    00a42820
    10a7000a
    0064202a
    10800001
    20050000
    00e2202a
    00853820
    00e23822
    ac670044
    8c020050
    08000011
    20020001
    ac020054

## Codes Convert to Instructions

> Can read **Binary** and **Hexadecimal** code.

Run

    python code2instr.py <filename>

An Example:

    python code2instr.py codes.txt

Results:

    20020005
    2003000C
    2067fff7
    00e22025
    00642824
    00a42820
    10a7000a
    0064202a
    10800001
    20050000
    00e2202a
    00853820
    00e23822
    ac670044
    8c020050
    08000011
    20020001
    ac020054
    
    ADDI R2 R0 5
    ADDI R3 R0 12
    ADDI R7 R3 65527
    OR R4 R7 R2
    AND R5 R3 R4
    ADD R5 R5 R4
    BEQ R5 R7 10
    SLT R4 R3 R4
    BEQ R4 R0 1
    ADDI R5 R0 0
    SLT R4 R7 R2
    ADD R7 R4 R5
    SUB R7 R7 R2
    SW R7 68 R3
    LW R2 80 R0
    J 11
    ADDI R2 R0 1
    SW R2 84 R0


## Design your code format

You can also add other instructions to the json file

> Many Rtype commands started with a special opcode '000000', the numbers in json refer to their Func codes.

    // These can be different without repeating.
    {
      "I": {
        "ADDI": "001000",
        "SUBI": "001011",
        "SLT1": "001100",
        "LW": "100011",
        "SW": "101011",
        "BNEQZ": "001101",
        "BEQ": "000100"
      },
      "R": {
        "Rtype": "000000" // Do not delete this line, otherwise Rtype commands will be unavailable
      },
      "J": {
        "HLT": "111111",
        "J": "000010"
      },
      "Rtype": { // Numbers below refer to Func codes in Rtype command
        "ADD": "010011",
        "SUB": "000001",
        "AND": "111010",
        "OR": "000011",
        "SLT": "010100",
        "MUL": "000101"
      }
    }

## 9-dimensional Matrix ADD Operation
### Instructions
The instructions are in [matrix_add.txt](matrix_add.txt)

    ADDI R19 R0 9   // D = 9 dimension
    ADDI R20 R0 0   // Init index i = 0
    ADD R21 R20 R19 // Init index j = i + D
    LW R1 0 R20     // Read Mem(i)
    LW R10 0 R21    // Read Mem(j)
    ADD R1 R1 R10   // Add Mem(i) and Mem(j)
    SW R1 0 R20     // Write the result back to Mem(i)
    ADDI R20 R20 1  // i = i + 1
    BEQ R19 R20 1*   // if i == D  pc = (pc + 1)+ 1*  
    J 2             // Go back to line 3
    LW R31 0 R0     // Read the matrix elements...
    LW R31 1 R0
    LW R31 2 R0
    LW R31 3 R0
    LW R31 4 R0
    LW R31 5 R0
    LW R31 6 R0
    LW R31 7 R0
    LW R31 8 R0

### Machine codes for MIPS
Codes are in [matrix_add_code.txt](matrix_add_code.txt)

    20130009
    20140000
    0293a820
    8e810000
    8eaa0000
    002a0820
    ae810000
    22940001
    12740001
    08000002
    8c1f0000
    8c1f0001
    8c1f0002
    8c1f0003
    8c1f0004
    8c1f0005
    8c1f0006
    8c1f0007
    8c1f0008
