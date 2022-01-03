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
    
    00000000010000110000100000000000
    00100000011000000000000000001011
    
    00430800
    2060000b

## Codes Convert to Instructions

Run

    python code2instr.py <filename>

An Example:

    python code2instr.py codes.txt

Results:

    00000000010000110000100000000000
    00100000011000000000000000001011
    00430800
    2060000b
    
    ADD R2 R3 R1 0 000000
    LW R3 R0 11
    ADD R2 R3 R1 0 000000
    LW R3 R0 11

## Design your code format

You can also add other instructions to the json file

    {
      "I": {
        "LW": "001000",
        "SW": "001001",
        "BNEQZ": "001101",
        "BEQZ": "001110"
      },
      "R": {
        "ADD": "000000",
        "SUB": "000001",
        "AND": "000010",
        "OR": "000011",
        "SLT": "000100",
        "MUL": "000101",
        "ADDI": "001010",
        "SUBI": "001011",
        "SLT1": "001100"
      },
      "J": {
        "HLT": "111111",
        "J": "111110"
      }
    }
