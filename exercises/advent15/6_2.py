"""

"turn on 887,9 through 959,629"
"toggle 0,0 through 999,0"
"turn off 499,499 through 500,500"


"""

def parse_instruction(token_list):
    for i, token in enumerate(token_list):
        if token in ['toggle', 'on', 'off']:
            upper_left = [int(num) for num in token_list[i+1].strip().split(',')]
            instruction = token
        elif token == 'through':
            bottom_right = [int(num) for num in token_list[i+1].strip().split(',')]
    return instruction, upper_left, bottom_right


def execute_instruction(instruction_list):
    for row in range(instruction_list[1][1], instruction_list[2][1] + 1):
        for column in range(instruction_list[1][0], instruction_list[2][0] + 1):
            if instruction_list[0] == 'on':
                LIGHT_ARRAY[row][column] += 1
            elif instruction_list[0] == 'off':
                if LIGHT_ARRAY[row][column] > 0:
                    LIGHT_ARRAY[row][column] -= 1
            else:
                LIGHT_ARRAY[row][column] += 2

LIGHT_ARRAY = [[0for i in range(1000)] for j in range(1000)]
instructions = [line.rstrip('\n') for line in open('input.txt')]
for inst in instructions:
    parsed_inst = parse_instruction(inst.split())
    execute_instruction(parsed_inst)


total_lights = 0
print(sum(sum(row) for row in LIGHT_ARRAY))

