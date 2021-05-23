#!/usr/bin/env python3


import random as r
from typing import List



def shuffled(li: List[int]) -> List[int]:
    li_new: List[int] = [n for n in li]
    r.shuffle(li_new)
    return li_new


def main() -> None: 
    li: List[int] = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    print(f"Original:\t {li}")
    print(f"Last element of shuffled:\t {shuffled(li)[-1]}")
    print(f"Shuffled again:\t {shuffled(li)}")
    print(f"Original:\t {li}")




#############################################################x

if __name__ == "__main__":
    main()

