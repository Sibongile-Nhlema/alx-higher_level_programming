#!/usr/bin/python3
''' Implements and solves the N queens puzzle
    Finds all possible solutions to placing N
    Backtracks any other paths that cause the queens to attack
    Usage:
        nqueens N
'''
import sys
'''Module need to run code '''

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    print("Hello There!")
