#!/usr/bin/env python3


def xor(a, b):
    return bool(a) != bool(b)

def main():
    str1 = "python"
    str2 = None
    print("{0} \t xor \t {1} \t = {2}\n".format(str1, str2, xor(str1, str2)))

    print("True \t xor \t False \t = {0}".format(xor(True, False)))
    print("True \t xor\t True \t = {0}".format(xor(True, True)))
    print("False \t xor\t False \t = {0}".format(xor(False, False)))
    print("0.0 \t xor \t '' \t = {0}".format(xor(0.0, '')))
    print("abc \t xor \t \"\" \t = {0}".format(xor("abc", "")))
    print("123 \t xor \t [] \t = {0}".format(xor(1, [])))
    


#############################################################################

if __name__ == "__main__":
    main()