class HelperMethods:
    @staticmethod
    def is_valid_input(input, min_length):
        clean_input = input.strip()
        input_length = len(clean_input)

        is_empty_input = clean_input == ""
        is_short_input = input_length < min_length

        return not (is_empty_input or is_short_input)