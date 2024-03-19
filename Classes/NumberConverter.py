from Utils.NumberStringConverter import number_to_string_converter


class NumberConverter:

    def __init__(self, number):
        self.number = number
        return

    def convert(self):
        converted_num = number_to_string_converter(self.number)
        return converted_num
