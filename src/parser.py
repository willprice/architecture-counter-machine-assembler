from string import join
import re


class Parser(object):
    def __init__(self, source_code=''):
        self.labels = {}
        self.source_code = source_code
        self.sanitize_code()

    def parse(self):
        self.sanitize_code()
        self.resolve_labels()
        self.substitute_labels()
        return self.source_code

    def sanitize_code(self):
        santitized_code = ''
        for line in self.source_code.split('\n'):
            line = self.remove_comment(line)
            line = self.remove_leading_and_trailing_whitespace(line)

            if (line != ''):
                santitized_code = join([santitized_code, line], '\n')

        self.source_code = santitized_code[1:]

    def break_line(self, line):
        line = self.remove_comment(line)
        line = self.remove_leading_and_trailing_whitespace(line)
        return line.split(' ')

    def remove_comment(self, line):
        return line.partition(';')[0]

    def remove_leading_and_trailing_whitespace(self, line):
        return line.strip(' ')

    def resolve_labels(self):
        line_number = 0
        for line in self.source_code.split('\n'):
            if self.line_begins_with_an_instruction(line):
                line_number += 1
            else:
                label = line[1:]
                self.labels[label] = line_number

    def line_begins_with_an_instruction(self, line):
        if line[0] == ':':
            return False
        return True

    def get_address_of_label(self, label):
        return self.labels[label]

    def get_labels(self):
        labels = []
        labels.append('label')
        return labels

    def remove_label_definitions(self):
        code_without_label_definitions = ''
        for line in self.source_code.split('\n'):
            if self.line_begins_with_an_instruction(line):
                code_without_label_definitions += line + '\n'
        self.source_code = code_without_label_definitions[:-1]


    def substitute_labels(self):
        self.remove_label_definitions()
        for label_definition in self.labels.iteritems():
            label = label_definition[0]
            label_value = label_definition[1]
            matcher = re.compile(r':' + label)
            self.source_code = matcher.sub(str(label_value), self.source_code)
