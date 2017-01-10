import math


def squaremid(x):
    if x < 128.0:
        return -math.sqrt(-((x - 128.0) / 128.0)) * 128.0 + 128.0
    return math.sqrt(((x - 128.0) / 128.0)) * 128.0 + 128.0


def squareup(x):
    return math.sqrt(x / 256.0) * 256.0


def squaredown(x):
    return ((x / 256.0) ** 2) * 256.0


warpfuncs = [squaredown,
             squaremid,
             squareup]
