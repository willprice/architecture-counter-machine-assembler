import unittest
from src import assembler
from src.assembler import Assembler

class InstructionTests(unittest.TestCase):
    def setUp(self):
        self.assembler = Assembler()

    def test_increment_r0_is_converted_to_0x0(self):
        self.assertEqual(0x0, self.increment(0))

    def test_increment_r1_is_converted_to_0x10(self):
        self.assertEqual(0x10, self.increment(1))

    def test_decrement_r0_is_converted_to_0x20(self):
        self.assertEqual(0x20, self.decrement(0))

    def test_decrement_r1_is_converted_to_0x30(self):
        self.assertEqual(0x30, self.decrement(1))

    def test_jnz_to_address_0_is_converted_to_0x40(self):
        self.assertEqual(0x40, self.jump_not_zero(0))

    def test_jnz_to_address_1_is_converted_to_0x41(self):
        self.assertEqual(0x41, self.jump_not_zero(1))

    def test_jnz_to_address_15_is_converted_to_0x4f(self):
        self.assertEqual(0x4f, self.jump_not_zero(0xf))

    def test_jneg_to_address_0_is_converted_to_0x60(self):
        self.assertEqual(0x60, self.jump_if_negative(0))

    def test_jneg_to_address_1_is_converted_to_0x61(self):
        self.assertEqual(0x61, self.jump_if_negative(1))

    def test_jneg_to_address_15_is_converted_to_0x6f(self):
        self.assertEqual(0x6f, self.jump_if_negative(15))

    def test_str_r0_to_address_0_is_converted_to_0x80(self):
        self.assertEqual(0x80, self.store(0, 0))

    def test_str_r1_to_address_0_is_converted_to_0x90(self):
        self.assertEqual(0x90, self.store(1, 0))

    def test_str_r0_to_address_1_is_converted_to_0x81(self):
        self.assertEqual(0x81, self.store(0, 1))

    def test_str_r1_to_address_15_is_converted_to_0x9f(self):
        self.assertEqual(0x9f, self.store(1, 15))

    def test_ldr_r0_to_address_0_is_converted_to_0xa0(self):
        self.assertEqual(0xa0, self.load(0, 0))

    def test_ldr_r1_to_address_0_is_converted_to_0xb0(self):
        self.assertEqual(0xb0, self.load(1, 0))

    def test_ldr_r0_to_address_1_is_converted_to_0xa1(self):
        self.assertEqual(0xa1, self.load(0, 1))

    def test_ldr_r1_to_address_15_is_converted_to_0xbf(self):
        self.assertEqual(0xbf, self.load(1, 15))

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
