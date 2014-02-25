class Assembler(object):
    def __init__(self):
        self.instruction_conversions = {"INC": self.inc,
                                        "DEC": self.dec,
                                        "JNZ": self.jnz,
                                        "JNEG": self.jneg,
                                        "STR": self.str,
                                        "LDR": self.ldr}

    def assemble(self, source_code):
        hex_code = ""
        for line in source_code.split('\n'):
            instruction_statement = line.split(' ')
            hex_code += hex(self.convert_mnemonic_into_instruction(instruction_statement))[2:] + '\n'
        return hex_code

    def inc(self, register):
        return register << 4

    def dec(self, register):
        return 0x20 | register << 4

    def jnz(self, address):
        return 0x40 | address

    def jneg(self, address):
        return 0x60 | address

    def str(self, register, address):
        return 0x80 | register << 4 | address

    def ldr(self, register, address):
        return 0xa0 | register << 4 | address

    def convert_from_string_to_int(self, operands):
        return map(int, operands)

    def convert_mnemonic_into_instruction(self, instruction_statement):
        instruction = instruction_statement[0]
        operands = instruction_statement[1:]

        instruction_function = self.instruction_conversions[instruction]
        operands = self.convert_from_string_to_int(operands)
        return instruction_function(*operands)
