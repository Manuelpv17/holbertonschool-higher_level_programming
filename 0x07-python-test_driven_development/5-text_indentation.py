#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :
    """


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :

        Arguments:
                text {str} -- text to be printed

        Raises:
                TypeError: text must be a string
        """
    if type(text) is not str:
        raise TypeError("text must be a string")
    new = ""
    for c in text:
        new += c
        if c == '.' or c == '?' or c == ':':
            new += "\n\n"

    new = new.split("\n")
    for i, item in enumerate(new):
        if i == len(new) - 1:
            break
        print(item.strip(" "))
    print(item.strip(" "), end="")
