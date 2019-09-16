from random import randint

def transform_roman(num):
    var = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    symbol = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman = ''
    i = 0
    while num > 0 and num <= 3000:
        for _ in range(num // var[i]):
            roman += symbol[i]
            num -= var[i]
        i += 1

    return roman
