def separate_letters_numbers(s):
    separates = {
        "numbers": "",
        "letters": ""
    }
    for char in s:
        if char.isdigit():
            separates["numbers"] + = char
        else:
            separates["letters"] + = char

    return separates


s = "a1B2c3D4"
print(separate_letters_numbers(s))
