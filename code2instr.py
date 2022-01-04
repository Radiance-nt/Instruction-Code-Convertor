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
    inverse = {}
    inverse_Func = {}
    for key, value in data.items():
        if key != 'Rtype':
            new_data.update(value)
            for k, v in value.items():
                if v in inverse:
                    raise NameError
                inverse[v] = k
        else:
            for k, v in value.items():
                if v in inverse_Func:
                    raise NameError
                inverse_Func[v] = k

with open(filename, 'rt') as file:
    for line, command_input in enumerate(file):  # This loop will go on forever
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
        if operate == 'Rtype':
            Rs = command[6:11]
            Rt = command[11:16]
            Rd = command[16:21]
            Shamt = command[21:26]
            Func = command[26:]
            Rs, Rt, Rd = 'R' + Bin2Int(Rs), 'R' + Bin2Int(Rt), 'R' + Bin2Int(Rd)
            Shamt = Bin2Int(Shamt)
            if Func not in inverse_Func:
                print('Line %d, Input %s' % (line, command_input), end=':')
                print('Func %s not Found in Rtypes!' % Func)
                raise NameError
            strlist = [inverse_Func[Func], Rs, Rt, Rd]
        elif operate in data['R']:
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
            ### TODO ### ############# ADD OR IMM #############
            # if operate in ['ADDI', 'SUBI', 'SLTI']:
            #     sign = 1 if ImmAddr16[0] == '0' else -1
            #     ImmAddr16 = sign * Bin2Int(ImmAddr16[1:])
            # else:
            #    ImmAddr16 = Bin2Int(ImmAddr16)
            ###################################################
            ImmAddr16 = Bin2Int(ImmAddr16)
            strlist = [operate, Rs, Rt, ImmAddr16]
        elif operate in data['J']:
            Addr26 = command[6:]
            Addr26 = Bin2Hex(Addr26)
            strlist = [operate, Addr26]
        else:
            print("Opcode not available!")
        if strlist[0] in data['Rtype']:  # Swapping string segments to get he desired hex code
            # RS1, RS2, Destination = RS2, Destination, RS1
            strlist[1], strlist[2], strlist[3] = strlist[3], strlist[1], strlist[2]
        elif strlist[0] in ['ADDI', 'SUBI', 'SLTI']:
            # RS1, RS2 = RS2, RS1
            strlist[1], strlist[2] = strlist[2], strlist[1]
        elif strlist[0] in ['LW', 'SW']:
            # RS1, RS2, Destination = Destination, RS1, RS2
            strlist[1], strlist[2], strlist[3] = strlist[2], strlist[3], strlist[1]
        output = ' '.join(strlist)
        outs.append(output)
    print()
    for result in outs:
        print(result)
