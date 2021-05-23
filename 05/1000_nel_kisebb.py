#!/usr/bin/env python3

"""
Prints numbers that are the multiples of 3 or 5 and are less than 1000.

"""
    

def main():
    print("Azon 1000-nel kisebb szamok osszege, melyek 3-nak vagy 5-nek tobbszorosei: ")
    print(sum([n for n in range(0, 1000) if n%3 == 0 or n%5 == 0]))



if __name__ == "__main__":
    main()

