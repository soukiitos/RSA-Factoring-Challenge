#!/usr/bin/python3
import sys
import subprocess


def check_factor(args):
    if len(args) != 3:
        count = 0
        num2 = 1
        for a in args:
            if count > 1:
                num2 *= int(a)
            count += 1
    else:
        num2 = int(args[2])
    num1 = int(args[1])
    num = args[0].replace(':', '=')
    result = 1 if num2 > num1 else 0
    if result == 1:
        numcp = num1
        num1 = num2
        num2 = numcp
    print(f"{num}{num1}*{num2}")


if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)


filename = sys.argv[1]
with open(filename, 'r') as file:
    lines = file.readlines()
for line in lines:
    result = subprocess.check_output(['factor', line], universal_newlines=True)
    check_factor(result.strip().split())
