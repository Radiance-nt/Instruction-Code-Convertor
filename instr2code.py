import argparse
import numpy as np  # Need to the conversion among different number bases - 10, 2, 16
import json  # Need to read and access the Json file, where the opcodes are written
import re  # Need to split the input string in different meaningful segments

FILENAME = 'instructions.txt'
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str, default=FILENAME, help='filename')
parser.add_argument('--print_binary', action="store_true")
parser.add_argument('--print_hex', action="store_true")

args = parser.parse_args()
filename = args.filename
print_binary = args.print_binary
print_hex = args.print_hex

bins = []
hexs = []

with open('./opcode.json') as f:
    data = json.load(f)  # Reading the Json file
    new_data = {}
    for v in data.values():
        new_data.update(v)

with open(filename, 'rt') as file:
    for command_input in file:
        command_input = command_input.rstrip('\n')
        if command_input=='':
            continue
        print(command_input)
        result_binary = '0'
        result_binary = result_binary.rjust(32, '0')
        # command_input = input("Enter: ")                            # Asking user to input the string
        command = re.split(',\\ |\\ |\\(', command_input)  # Split the srting by commas, space and brackets

        opcode = command[0]
        if len(command) == 3:  # For BEQZ and BNEQZ commands
            RS = command[1]
            Destination = command[2]
            type_of_opcode = 2
        elif len(command) == 4:  # For all other commands
            RS1 = command[1]
            RS2 = command[2]
            Destination = command[3]
            type_of_opcode = 1
        elif len(command) == 2:
            Destination = command[1]
            type_of_opcode = 0
        else:
            type_of_opcode = -1

        if opcode in ['ADD', 'SUB', 'AND', 'OR', 'SLT', 'MUL']:  # Swapping string segments to get he desired hex code
            RS1, RS2, Destination = RS2, Destination, RS1
        elif opcode in ['ADDI', 'SUBI', 'SLTI']:  # Swapping string segments to get he desired hex code
            RS1, RS2 = RS2, RS1
        elif opcode in ['LW', 'SW']:  # Swapping string segments to get he desired hex code
            if (')' in Destination):
                Destination = Destination[:-1]
            RS1, RS2, Destination = Destination, RS1, RS2
        else:
            if opcode not in new_data:  # Return to start the loop again, if false opcode is entered.
                print("Wrong opcode..")
                continue

        result_binary = new_data[opcode] + result_binary[6:]  # Manipulation of strings to get the proper opcode
        if type_of_opcode == 2:
            RS = RS[1:]
            RS = "{0:b}".format(int(RS))
            if len(RS) < 5:
                while len(RS) != 5:
                    RS = '0' + RS
            result_binary = result_binary[:6] + RS + result_binary[11:]
            result_binary = result_binary[:16] + np.binary_repr(int(Destination), width=16)

        elif type_of_opcode == 1:
            RS1 = RS1[1:]
            RS1 = "{0:b}".format(int(RS1))
            if len(RS1) < 5:
                while len(RS1) != 5:
                    RS1 = '0' + RS1
            result_binary = result_binary[:6] + RS1 + result_binary[11:]
            RS2 = RS2[1:]
            RS2 = "{0:b}".format(int(RS2))
            if len(RS2) < 5:
                while len(RS2) != 5:
                    RS2 = '0' + RS2
            result_binary = result_binary[:11] + RS2 + result_binary[16:]
            if Destination[0] == 'R':
                Destination = Destination[1:]
                Destination = "{0:b}".format(int(Destination))
                if len(Destination) < 5:
                    while len(Destination) != 5:
                        Destination = '0' + Destination
                result_binary = result_binary[:16] + Destination + result_binary[21:]
            elif Destination[0] != 'R':
                result_binary = result_binary[:16] + np.binary_repr(int(Destination), width=16)
        elif type_of_opcode == 0:
            Destination = bin(int(Destination, 16))[2:]
            result_binary = result_binary[:6] + result_binary[6:32 - len(Destination)] + Destination

        result_hex = hex(int(result_binary, 2))
        result_hex = result_hex[2:]
        if len(result_hex) in [7, 6]:
            while len(result_hex) != 8:
                result_hex = '0' + result_hex
        # result_hex = "32'h" + result_hex
        result_hex = result_hex
        bins.append(result_binary)
        hexs.append(result_hex)
    print()
    if print_binary:
        for result in bins:
            print(result)
        print()
    if print_hex:
        for result in hexs:
            print(result)
        print()
