import unittest
from src.assembler import Assembler
from parameterizedtestcase import ParameterizedTestCase


class AssemblyTests(ParameterizedTestCase):
    @ParameterizedTestCase.parameterize(
        ("expected_output", "input"),
        [
            (0x10, ["INC", "1"]),
            (0x00, ["INC", "0"]),
            (0x20, ["DEC", "0"]),
            (0x40, ["JNZ", "0"]),
            (0x60, ["JNEG", "0"]),
            (0x81, ["STR", "0", "1"]),
            (0xbf, ["LDR", "1", "15"])
        ]
    )
    def test_instruction_conversion(self, expected_output, input):
        assembler = Assembler()
        self.assertEqual(expected_output, assembler.convert_mnemonic_into_instruction(input))
