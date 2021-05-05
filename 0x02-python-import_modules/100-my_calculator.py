#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    op = argv[2]
    func = {"+": add, "-": sub, "*": mul, "/": div}
    if op not in func:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    print("{:d} {} {:d} = {:d}".format(a, op, b, func[op](a, b)))
