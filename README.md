# Instruction-Code Convertor


Modified on this repo:

https://github.com/souvicksaha95/Opcode-Generator-for-MIPS32-RISC-processor

## Instructions Convert to Codes
Run

    python instr2code.py <filename>  [--print_binary] [--print_hex]

An Example:

    python instr2code.py instructions.txt  --print_binary --print_hex

Results:

    ADD R1 R2 R3
    LW R3 0
    
    00000000010000110000100000010011
    10001100011000000000000000001011
    
    00430813
    8c60000b

## Codes Convert to Instructions

> Can read **Binary** and **Hexadecimal** code.

Run

    python code2instr.py <filename>

An Example:

    python code2instr.py codes.txt

Results:

    00000000010000110000100000010011
    10001100011000000000000000001011
    00430813
    8c60000b
    
    ADD R2 R3 R1 0
    LW R3 R0 11
    ADD R2 R3 R1 0
    LW R3 R0 11

## Design your code format

You can also add other instructions to the json file

> Many Rtype commands started with a special opcode '000000', the numbers in json refer to their Func codes.

    {
      "I": {
        "LW": "100011",
        "SW": "101011",
        "BNEQZ": "001101",
        "BEQ": "000100"
      },
      "R": {
        "Rtype": "000000", // Do not delete this line, otherwise Rtype commands will be unavailable
        "ADDI": "001000",
        "SUBI": "001011",
        "SLT1": "001100"
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
