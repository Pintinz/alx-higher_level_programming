#!/usr/bin/python3

if __name__ = '__main__':
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    result_added = add(a, b)
    result_mul = mul(a, b)
    result_sub = sub(a, b)
    result_div = div(a, b)

    print("{} + {} = {}".format(result_added))
    print("{} - {} = {}".format(result_sub))
    print("{} * {} = {}".format(result_mul))
    print("{} / {} = {}".format(result_div))
