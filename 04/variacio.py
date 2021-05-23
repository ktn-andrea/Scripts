#!/usr/bin/env python3


def main():
    li = list(range(1, 100+1))
    a = list(str(li))
    res = 0
    for i in a:
        if i in '0123456789':
            res += int(i)
        

    print("Szamjegyek osszege 1-tol 100-ig: {0}".format(res))
    print("Szamok osszege 1-tol 100-ig: {0}".format(sum(range(1,100+1))))





###################################################################
if __name__ == "__main__":
    main()