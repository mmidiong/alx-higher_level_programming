#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        firstchar = None
        _tuple = (length, firstchar)
        return _tuple
    else:
        firstchar = sentence[0]
        _tuple = (length, firstchar)
        return _tuple
