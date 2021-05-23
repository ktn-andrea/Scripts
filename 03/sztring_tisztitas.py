#!/usr/bin/env python3


def format_text(s):
    s = s.replace(" ", "")
    i = 0
    while i <= len(s)-1:
        if s[i] == "\\" and s[i+1] in ["'", "\\", "n", "r", "t", "b", "f"]:
            s = s.replace(s[i:i+2], '')
        elif s[i] == "\\" and s[i+1:i+4] in ["ooo", "xhh"]:
            s = s.replace(s[i:i+4], '')
        else:
            i += 1
    return s


def main():
    text = input("Bemeneti sztring: ")
    print(format_text(text))

#############################################################################

if __name__ == '__main__':
    main()
