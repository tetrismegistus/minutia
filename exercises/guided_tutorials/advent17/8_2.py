from collections import namedtuple, defaultdict

Instruction = namedtuple('Instruction', ['dest_register',
                                         'instruction',
                                         'inst_value',
                                         'condition',
                                         'comp_register',
                                         'operator',
                                         'comp_value'])


def read_input(filename):
    lines = [line.rstrip('\n').split() for line in open(filename)]
    instructions = []
    for line in lines:
        line[1] = '+=' if line[1] == 'inc' else '-='
    for line in lines:
        instructions.append(Instruction._make(line))
    return instructions


def run_instructions(instruction_list):
    registers = defaultdict(int)
    max_value = 0
    for instruction in instruction_list:
                # 'a  +=  1 if a  >  1  else a'
        dest_string = 'registers[instruction.dest_register]'
        comp_string = 'registers[instruction.comp_register]'
        execute = '{} {} {} if {} {} {} else 0'.format(dest_string,
                                                       instruction.instruction,
                                                       instruction.inst_value,
                                                       comp_string,
                                                       instruction.operator,
                                                       instruction.comp_value)
        exec(execute)
        if max(registers.values()) > max_value:
            max_value = max(registers.values())
    return max_value

inst_set = read_input('input.txt')
reg_state = run_instructions(inst_set)
print(reg_state)


