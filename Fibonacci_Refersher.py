#!/usr/bin/env python
import argparse

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help="The Fibonacci number you want to calculate.", type=int)
    parser.add_argument("-o", "--output", help="Output result to a file.", action="store_true")
    args = parser.parse_args()
    result = fibonacci(args.num)
    print("The "+str(args.num)+"th fibonacci number is "+str(result))

    if args.output:
        f = open("fibonacci.txt", "a")
        f.write(str(result)+'\n')
        f.close()

if __name__ == '__main__':
    main()
