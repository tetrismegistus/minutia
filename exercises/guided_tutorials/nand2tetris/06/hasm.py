import argparse

from modules import parser, code, symbolTable


def remove_file_extension(filename):
    return filename.split('.')[0]


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def first_pass(filename):
    symbol_table = symbolTable.SymbolTable.copy()
    ROM_address = 0
    parser_object = parser.Parser(filename)
    while parser_object.has_more_commands:
        parser_object.advance()
        if (parser_object.command_type == parser.CommandType.C_COMMAND or
                parser_object.command_type == parser.CommandType.A_COMMAND):
            ROM_address += 1
        elif parser_object.command_type == parser.CommandType.L_COMMAND:
            symbol = '0{0:015b}\n'.format(ROM_address)
            symbol_table[parser_object.symbol] = symbol
    return symbol_table


def second_pass(filename, symbol_table):
    parser_object = parser.Parser(filename)
    symbols = symbol_table
    next_address = 16
    out_filename = remove_file_extension(filename) + '.hack'
    with open(out_filename, 'w') as out_file:
        while parser_object.has_more_commands:
            parser_object.advance()
            if parser_object.command_type == parser.CommandType.A_COMMAND and not is_int(parser_object.symbol):

                if parser_object.symbol in symbols:
                    symbol = symbols[parser_object.symbol]
                else:
                    symbol = '0{0:015b}\n'.format(next_address)
                    symbols[parser_object.symbol] = symbol
                    next_address += 1
                out_file.write(symbol)
            elif parser_object.command_type == parser.CommandType.A_COMMAND and is_int(parser_object.symbol):
                symbol = '0{0:015b}\n'.format(int(parser_object.symbol))
                out_file.write(symbol)
            elif parser_object.command_type == parser.CommandType.C_COMMAND:
                comp_code = code.Code(parser_object)
                out_file.write('111{}{}{}\n'.format(comp_code.comp(), comp_code.dest(), comp_code.jump()))


def main():
    arg_parser = argparse.ArgumentParser(prog='hasm.py', usage='%(prog)s')
    arg_parser.add_argument('filename')
    args = arg_parser.parse_args()
    symbols = first_pass(args.filename)
    second_pass(args.filename, symbols)


if __name__ == '__main__':
    main()
