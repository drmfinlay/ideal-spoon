import sys

shifted_symbols = [
    "~", "!", "@", "#", "$","%", "^", "&", "*", "(", ")", "_", "+", "{", "}", "|", ":", '"', "<", ">", "?"
]

if __name__ == '__main__':
    # Join all arguments into a single string except the first argument which is this file's path
    assert len(sys.argv) >= 2
    input_string = " ".join(sys.argv[1:])
    print input_string
    output_string = "key"
    for c in input_string:
        assert isinstance(c, str)
        if c.islower() or c.isdigit():
            output_string += " " + c
        elif c in shifted_symbols or c.isupper():
            output_string += " shift " + c + " -shift"
        elif c.isspace():
            output_string += " space"
        else:
            output_string += " " + c
    print output_string
