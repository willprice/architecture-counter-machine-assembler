from parameterizedtestcase import ParameterizedTestCase
from src.parser import Parser


class ParserTests(ParameterizedTestCase):
    def setUp(self):
        self.Parser = Parser

    @ParameterizedTestCase.parameterize(("expected_output", "line"),
                                        [
                                            (["INC", "1"], "INC 1"),
                                            (["INC", "0"], "INC 0"),
                                            (["INC", "1"], "INC 1 ; this is a comment"),
                                            (["INC", "1"], "  INC 1"),
                                         ])
    def test_split_instruction_line(self, expected_output, line):
        self.assertEqual(expected_output, self.Parser().break_line(line))

    def label_table_test_cases(*args):
        return [(0, "label",
                 """:label
                    INC 1"""),
                (1, "label",
                 """INC 0
                    :label
                    INC 1"""),
                (0, "l",
                 """:l
                    INC 0""")
                ]

    @ParameterizedTestCase.parameterize(("expected_address", "label", "code"), label_table_test_cases())
    def test_labels_are_added_to_assembler_table(self, expected_address, label, code):
        parser = self.Parser(source_code=code)
        parser.resolve_labels()
        self.assertEqual(expected_address, parser.get_address_of_label(label))

    @ParameterizedTestCase.parameterize(("expected_code", "code"),
                                        [
                                            ("INC 0",
                                             """:label
                                                INC :label
                                             """),
                                            ("INC 0\n" "JNZ 0",
                                             """:label
                                                INC 0
                                                JNZ :label"""),
                                        ])
    def test_labels_are_substituted(self, expected_code, code):
        parser = self.Parser(source_code=code)
        parser.resolve_labels()

