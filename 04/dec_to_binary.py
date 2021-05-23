#!/usr/bin/env python3

def binary_to_decimal1(dec):
    if dec == 0:
        return 0
    li = []
    while dec != 0:
        rem = int(dec % 2)
        li.append(rem)
        dec = (dec - rem) / 2
    res = ""
    for l in li[::-1]:
        res += str(l)
    return res


def binary_to_decimal2(dec):
    return bin(dec)[2::]



def main():
    a = int(input("Bemeneti szam(decimalis, pozitiv): "))

    print("Binaris alak: {0}".format(binary_to_decimal1(a)))

    print("Binaris alak: {0}".format(binary_to_decimal2(a)))




#############################################################################

if __name__ == "__main__":
    main()
