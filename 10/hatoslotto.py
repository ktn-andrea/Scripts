#!/usr/bin/env python3

import random as r


SUM = 90
PRODUCT = 996_300


def product(li):
    res = 1
    for num in li:
        res *= num
    return res



def main(): 
    nums = [n for n in range(1, 45+1) if (PRODUCT % n) == 0]
    li = []
    while True:
        for i in range(6):
            li.append(r.choice(nums))
        if sum(li) == SUM and product(li) == PRODUCT:
            break
        li.clear()

    print("Nyeroszamok:", li)


########################################################################

if __name__ == "__main__":
    main()


