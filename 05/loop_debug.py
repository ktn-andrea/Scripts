#!/usr/bin/env python3


def loop(n, debug=False):
    """Returns numbers between 1 and given number"""

    if debug:
        print("# ciklus kezdete:")

    print(' '.join([str(i) for i in range(1, n+1)]))

    if debug:
        print("# ciklus vege")

    

def main(): 
    loop(5)
    loop(5, debug=True)

#########################################

if __name__ == "__main__":
    main()

