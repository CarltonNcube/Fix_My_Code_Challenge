#!/usr/bin/python3
""" FizzBuzz
"""
import sys

def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.

    - For multiples of three, print "Fizz" instead of the number.
    - For multiples of five, print "Buzz" instead of the number.
    - For numbers which are multiples of both three and five, print "FizzBuzz".
    """
    if n < 1:
        return

    for i in range(1, n + 1):
        output = ""
        if (i % 3) == 0:
            output += "Fizz"
        if (i % 5) == 0:
            output += "Buzz"

        if output:
            print(output)
        else:
            print(i)

if __name__ == '__main':
    if len(sys.argv) != 2:
        print("Usage: ./0-fizzbuzz.py <number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        fizzbuzz(number)
    except ValueError:
        print("Invalid input. Please provide a valid integer.")
