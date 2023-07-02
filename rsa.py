#!/usr/bin/python3
import sys


def factor(n):
    n = int(n)
    factors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i, n // i))
    
    for p, q in factors:
        print(f"{n} = {p} * {q}")


def main():
    if len(sys.argv) != 2:
        print("Usage: factors <filename>")
        sys.exit(1)

        filename=sys.argv[1]
    try:
        with open(filename, 'r') as file:
            numbers = file.readlines()
        for number in numbers:
            factor(number.strip())
    except I0Error:
        sys.stderr.write(f"Error: can't open file {filename}\n")
        sys.exit(1)


if __name__ == '__main__':
    main()
