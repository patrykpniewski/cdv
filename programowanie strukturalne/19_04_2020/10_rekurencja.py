# potęgowanie

"""
    pow(3, 3) --> 3 * 3 * 3 * 1
    pow(3, 2) --> 3 * 3 * 1
    pow(3, 1) --> 3 * 1
    pow(3, 0) --> 1
"""


def potega(x, y):
    if y == 0:
        return 1
    else:
        return x * pow(x, y-1)


for i in range(10):
    print(potega(3, i))
