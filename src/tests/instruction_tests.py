import unittest
from src import assembler
from src.assembler import Assembler
from parameterizedtestcase import ParameterizedTestCase

class InstructionTests(ParameterizedTestCase):
    def setUp(self):
        self.assembler = Assembler()

    @ParameterizedTestCase.parameterize(("expected_instruction", "register_to_increment"),
                                        [(0x0, 0), (0x10, 1)])
    def test_increment(self, expected_instruction, register_to_increment):
        self.assertEqual(expected_instruction, self.increment(register_to_increment))

    @ParameterizedTestCase.parameterize(("expected_instruction", "register_to_decrement"),
                                        [(0x20, 0), (0x30, 1)])
    def test_decrement(self, expected_instruction, register_to_decrement):
        self.assertEqual(expected_instruction, self.decrement(register_to_decrement))

    @ParameterizedTestCase.parameterize(("expected_instruction", "jump_address"),
                                        [(0x40, 0), (0x41, 1), (0x4f, 15)])
    def test_jump_not_zero(self, expected_instruction, jump_address):
        self.assertEqual(expected_instruction, self.jump_not_zero(jump_address))

    @ParameterizedTestCase.parameterize(("expected_instruction", "jump_address"),
                                        [(0x60, 0), (0x61, 1), (0x6f, 15)])
    def test_jump_negative(self, expected_instruction, jump_address):
        self.assertEqual(expected_instruction, self.jump_if_negative(jump_address))

    @ParameterizedTestCase.parameterize(("expected_instruction", "register", "address"),
                                        [(0x80, 0, 0), (0x90, 1, 0), (0x9f, 1, 15)])
    def test_store_from_register(self, expected_instruction, register, address):
        self.assertEqual(expected_instruction, self.store(register, address))

    @ParameterizedTestCase.parameterize(("expected_instruction", "register", "address"),
                                        [(0xa0, 0, 0), (0xb0, 1, 0), (0xa1, 0, 1), (0xbf, 1, 15)])
    def test_load_to_register(self, expected_instruction, register, address):
        self.assertEqual(expected_instruction, self.load(register, address))

    def load(self, register, address):
        return self.assembler.ldr(register, address)

    def store(self, register, address):
        return self.assembler.str(register, address)

    def jump_if_negative(self, address):
        return self.assembler.jneg(address)

    def jump_not_zero(self, address):
        return self.assembler.jnz(address)

    def decrement(self, register):
        return self.assembler.dec(register)

    def increment(self, register):
        return self.assembler.inc(register)
