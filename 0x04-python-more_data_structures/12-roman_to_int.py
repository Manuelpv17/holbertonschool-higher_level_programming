#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    aux_num = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string and type(roman_string) == str:
        for i, letter in enumerate(roman_string):
            if letter in roman:
                number += roman[letter]
                if i > 0 and letter != roman_string[i - 1]:
                    if roman[letter] > aux_num:
                        number -= aux_num * 2
                    aux_num = 0
                aux_num += roman[letter]
            else:
                return(0)
    return(number)
