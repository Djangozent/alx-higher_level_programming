#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, div, mul

if __name__ == "__main__":
    if (not len(argv) == 4):
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)
        result = 0
        a = int(argv[1])
        op = argv[2]
        b = int(argv[3])
        if (op == "+"):
            result = add(a, b)
        elif (op == "-"):
            result = sub(a, b)
        elif (op == "/"):
            result = div(a, b)
        elif (op == "*"):
            result = mul(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        printf(f"{a} {op} {b} = {result}")
