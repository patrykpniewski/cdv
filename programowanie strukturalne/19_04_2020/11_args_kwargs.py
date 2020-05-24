def sum(*args):
    result = 0

    for x in args:
        result += x

    return result


print(sum(1, 2, 3, 4))


def test(**kwargs):
    for name, value in kwargs.items():
        print(f"{name}: {value}")


test(a=1, b=2, c=3, d=4, e=5)
