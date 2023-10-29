#!/usr/bin/python3

import sys
import time

    def factorize(num):
        """Takes a number as import,

        Args:
                num: input interger
                Return: A tuple of two factors if the number is not a prime.
                        None if the number is prime
        """
        for i in range (2, int(num**0.5)+ 1):
            if num % i == 0:
                return (i, num//i)
        return None

    if _name_ == "_main_":

        """Reads the input file.
        """

        if len(sys,argv) != 2:
            print("Usage: factors <file>")
            exit()

        input_file = sys.argv[1]

        try:
            with open(input_file, 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("file not found")
            exit()

        start_time = time.time()

        """loops over each line (which should contain natural number for line),
            and calls factorize on each number.
            if factorize returns a tuple of factors,
            it prints the factorize in the desired form
        """

        for line in lines:
            num = int(line.strip())
            factors = factorization(num)
            if factors:
                print{f"(num)-(factors[0]}*{factors[1]}"}

            """if the elapsed time exceeds 5 seconds,
                the prgram exits with an error message.
            """
            if time.time() - start_time > 5:
                print("Time limit exceeded")
                exit()
