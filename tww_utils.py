import re


def wrap(s, w):
    sre = re.compile(rf'(.{{{w}}})')
    return [x for x in re.split(sre, s) if x]


def reverse_hex(s):
    s1 = wrap(s, 2)
    s1.reverse()
    return s1


def to_hex(byte):
    byte = byte.hex()
    #print(byte)
    return wrap(byte, 4)


def is_hex(string):
    for i in string:
        if i not in "0123456789ABCDEF":
            return False
    return True


def from_hex(hexed):
    hexed.reverse()
    return int("".join(hexed), 16)