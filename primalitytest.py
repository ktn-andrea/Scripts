#!/usr/bin/env python3

from sys import exit


def miller_rabin(n, a) -> bool():
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d = d // 2
    print("s:", s, "\nd:", d )

    elso: int = elso_teszt(n, a, d)
    print('-'*30)
    print("Az elso teszt eredmenye: {}.".format(elso))
    print('-'*30)
    if elso == 1:
        return True
    elif elso == n-1:
        masodik = elso - n
        print("A masodik teszt eredmenye: {}.".format(masodik))
        print('-'*30)
        return True

    masodik: int = masodik_teszt(n, a, d, s)
    print("A masodik teszt eredmenye: {}.".format(masodik))
    print('-'*30)
    return masodik == n-1
    

def elso_teszt(n, a, d) -> int():
    res = (a ** d) % n
    return res


def masodik_teszt(n, a, d, s) -> int():
    for r in range(0, s):
        res = (a ** (d * 2**r) ) % n
        print("r = {}: {}".format(r, res))
        if res == n-1:
            break
    return res


def egesz(num) -> bool():
    return num % 1 == 0


def ervenyes(n, a) -> bool():
    if a < 2 or a > n-1:
        return False
    return True



def main(): 
    print("A program Miller-Rabin primtesztet hajt vegre.")
    try:
        n = int(input("n = "))
        a = int(input("a = "))
    except ValueError:
        print("Hibas input!")
        exit(0)
    
    if n <= 3 or egesz(n) == False:
        print("\"n\" erteke 3-nal nagyobb, egesz szam kell legyen.")
        exit(0)
    if n % 2 == 0:
        print("\"n\" erteke 3-nal nagyobb, paratlan szam kell legyen.")
        exit(0)
    if ervenyes(n, a) == False:
        print("\"a\" erteke 2 es p-1 kozotti egesz kell legyen.")
        exit(0)


    if miller_rabin(n, a) == True:
        print("A teszt alapjan a = {} valasztassal n = {} lehet prim.".format(a, n))
    else:
        print("A teszt alapjan n = {} biztosan nem prim.".format(n))

    print('-'*30)




########################################################################

if __name__ == "__main__":
    main()

