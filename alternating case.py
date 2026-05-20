def to_alternating_case(string):
    new_string = ""
    for char in string:
        if char.isupper():
            new_string += char.lower()
        elif char.islower():
            new_string += char.upper()
        else:
            new_string += char
    return new_string
        