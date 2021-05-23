#!/usr/bin/env python3


def is_palindrome1(s):
    return s == s[::-1]


def is_palindrome2(s):
    i = 0
    p = False
    while i <= len(s)/2:
        if s[i] == s[len(s)-i-1]:
            p = True
        else:
            return False
        i += 1
    return p


def is_palindrome3(s):
    if len(s) < 2:
        return True
    elif s[0] == s[-1]:
        return is_palindrome3(s[1:len(s)-1])
    else:
        return False



def main():
    s = input("Bemeneti szo: ")
    print("{0}: {1}".format(s,is_palindrome1(s)))
    print("{0}: {1}".format(s,is_palindrome2(s)))
    print("{0}: {1}".format(s,is_palindrome3(s)))
    

#################################################################


if __name__ == "__main__":
    main()
