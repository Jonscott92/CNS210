#!/usr/bin/python3
import argparse
#Fibonacci Function
def fibio(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibio(n-1) + fibio(n-2)
#Parsing the Fibonacci Function to a user number
parser = argparse.ArgumentParser()
parser.add_argument("-filename", help="created file with nth fibonacci number", type=str)
parser.add_argument("-number", help="number use to calculate nth fibonacci number", type=int)
args = parser.parse_args()
#Exception for overwrite the file if its the same filename
if args.filename:
    try:
        f = open(args.filename, "x")
        f.write(str(fibio(args.number)))
        f.close()
    except:
        overwrite = input("Would you wish to overwrite the file. yes/no\n")
        if overwrite == "yes":
            f = open(args.filename, "w")
            f.write(str(fibio(args.number)))
            f.close()
        elif overwrite == "no":
                exit()