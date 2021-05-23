#!/usr/bin/env python3


import random
from typing import List


def get_pages(li: List[str]) -> List[int]:
    res = []
    tol: int = 0
    ig: int = 0
    for i in li:
        if '-' not in i and i != '' and i.isdigit():
            res.append(int(i))
        elif '-' in i:
            li_acts = i.split('-')
            if li_acts[0].isdigit() and li_acts[-1].isdigit():
                tol = int(li_acts[0])
                ig = int(li_acts[-1])
            if tol > ig:
                ig, tol = tol, ig
            for j in range(tol, ig+1):
                res.append(j)

    return res




def main() -> None: 
    s: str = input("Adja meg a nyomtatando oldalakat (vesszőkkel és kötőjelekkel elválasztva):\n ")
    li: List[str] = s.replace(' ','').split(",")
    print("Nyomtatando oldalak:\n {}".format(get_pages(li)))



####################################################################

if __name__ == "__main__":
    main()

