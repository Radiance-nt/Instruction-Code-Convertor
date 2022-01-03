import argparse
import numpy as np  # Need to the conversion among different number bases - 10, 2, 16
import json  # Need to read and access the Json file, where the opcodes are written
import re  # Need to split the input string in different meaningful segments

result_binary = '0'  # Initializing the 32 bit string
result_binary = result_binary.rjust(32, '0')  # Padding zeros to all 32 places

FILENAME = 'codes.txt'
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str, default=FILENAME, help='filename')
args = parser.parse_args()
filename = args.filename


def Bin2Hex(result_hex: str):
    result_hex = hex(int(result_hex, 2))
    result_hex = result_hex[2:]
    return result_hex


def Hex2Bin(result_hex: str):
    result_hex = bin(int(result_hex, 16))
    result_hex = result_hex[2:]
    return result_hex


def Bin2Int(result_hex: str):
    result_hex = int(result_hex, 2)
    result_hex = str(result_hex)
    return result_hex


outs = []
with open('./opcode.json') as f:
    data = json.load(f)  # Reading the Json file
    new_data = {}
    for v in data.values():
        new_data.update(v)
    inverse = {}
    for key, value in new_data.items():
        if value in inverse:
            raise NameError
        inverse[value] = key

with open(filename, 'rt') as file:
    for command_input in file:  # This loop will go on forever
        command_input = command_input.rstrip('\n')
        print(command_input)
        if 'h' in command_input:
            command_input = command_input[command_input.find('h') + 1:]

        if len(command_input) == 32:
            command = command_input
        elif len(command_input) <= 8:
            command = Hex2Bin(command_input)
        else:
            print('Length error')
            raise Exception

        command = result_binary[:32 - len(command)] + command

        opcode = command[:6]
        operate = inverse[opcode]
        output = []
        if operate in data['R']:
            Rs = command[6:11]
            Rt = command[11:16]
            Rd = command[16:21]
            Shamt = command[21:26]
            Func = command[26:]
            Rs, Rt, Rd = 'R' + Bin2Int(Rs), 'R' + Bin2Int(Rt), 'R' + Bin2Int(Rd)
            Shamt = Bin2Int(Shamt)
            strlist = [operate, Rs, Rt, Rd, Shamt, Func]
        elif operate in data['I']:
            Rs = command[6:11]
            Rt = command[11:16]
            ImmAddr16 = command[16:]
            Rs, Rt = 'R' + Bin2Int(Rs), 'R' + Bin2Int(Rt)
            ImmAddr16 = Bin2Int(ImmAddr16)
            strlist = [operate, Rs, Rt, ImmAddr16]
        elif operate in data['J']:
            Addr26 = command[6:]
            Addr26 = Bin2Hex(Addr26)
            strlist = [operate, Addr26]
        else:
            print("Opcode not available!")
        output = ' '.join(strlist)
        outs.append(output)
    print()
    for result in outs:
        print(result)
