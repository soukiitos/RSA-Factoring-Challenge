#!/usr/bin/python3
import sys


def factor(buffer):
    num = int(buffer)
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} = {num // i} * {i}")
            break


def main():
    if len(sys.argv) != 2:
        print("Usage: factor <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        for line in lines:
            factor(line.strip())
    except I0Error:
        sys.stderr.write(f"Error: can't open file {filename}\n")
        sys.exit(1)


if __name__ == '__main__':
    main()
