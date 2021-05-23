#!/usr/bin/env python3


def decrypt(msg, shift):
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abc = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for i in msg:
        if i in abc:
            pos = abc.find(i)
            new_pos = (pos + 2) % len(abc)
            result += abc[new_pos]
        elif i in ABC:
            pos = ABC.find(i)
            new_pos = (pos + 2) % len(ABC)
            result += ABC[new_pos]
        else:
            result += i

    return result



def main():

    msg = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""

    print(decrypt(msg.strip(), 2))



##############################################################################

if __name__ == "__main__":
    main()
