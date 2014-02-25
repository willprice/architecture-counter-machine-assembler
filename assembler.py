import sys
from src.assembler import Assembler
from src.parser import Parser

if __name__ == '__main__':
    program_name = sys.argv[1]
    hex = ""

    with open(program_name, 'r') as program:
        parser = Parser(program.read())
        parsed_output = parser.parse()
        assembler = Assembler()
        hex = assembler.assemble(parsed_output)

    with open(program_name + '.hex', 'w') as hex_file:
        hex_file.write(hex)
        print "Written to " + program_name + '.hex'
