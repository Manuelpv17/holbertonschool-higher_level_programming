#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    roman = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    if roman_string:
        for letter in roman_string:
            if letter in roman:
                if number > 0 and roman[letter] > number:
                    number = roman[letter] - number
                else:
                    number += roman[letter]
            else:
                return(0)
    return(number)
