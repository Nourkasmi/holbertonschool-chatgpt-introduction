#!/usr/bin/python3
import sys

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        print(arg)
else:
    print("No arguments provided.")
