#!/usr/bin/python3
def multiple_returns(sentence):
    lens = len(sentence)
    if lens > 0:
        return((lens, sentence[0]))
    return((lens), None)
