#!/usr/bin/python3
import argparse

def fibonacci(n):
        a, b = 0, 1
        if n == 0:
            return 0
        for i in range(n):
            a, b = b, a+b
        return a

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-number", type=int, help="calculate fibonacci to the nth term")
    parser.add_argument("-file", "--filename", help="output sequence to a filename", action="store_true")
    args = parser.parse_args()
    results = fibonacci(args.number)
    print("The "+str(args.number)+"th fibonacci number is "+str(results))

    if args.filename:
        f = open("fibonacci.txt", "x")
        f.write(str(results))
        f.close()

if __name__ == "__main__":
    Main()
