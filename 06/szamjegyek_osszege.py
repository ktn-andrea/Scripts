#!/usr/bin/env python3



def main():
    num = 2 ** 1000
    digits = [int(i) for i in str(num)]

    print(sum(digits))





#############################################################################

if __name__ == '__main__':
    main()