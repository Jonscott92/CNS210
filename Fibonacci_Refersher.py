#!/usr/bin/python
import argparse
import os

def fibio(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibio(n-1) + fibio(n-2)
parser = argparse.ArgumentParser()
parser.add_argument("-filename", help="file you wish to write to", type=str)
parser.add_argument("-number", help="number of fibonacci sequence", dest='number', type=int)
args = parser.parse_args()
filepath = os.path.isfile(args.filename)

if os.path.isfile(args.filename):
    print("File Already Exist")
else:
    f = open(args.filename, "w")
    f.write(str(fibio(args.number)))
    f.close()
