#!/usr/bin/env python3



MAX = 1_000_000


def is_bin_pal(num: int) -> bool:
    b = int(bin(num)[2::])
    if len(str(b)) < 2:
        return True
    elif str(b) == str(b)[::-1]:
        return True
    return False
    

def is_dec_pal(num: int) -> bool:
    if len(str(num)) < 2:
        return True
    elif str(num) == str(num)[::-1]:
        return True
    return False


def main() -> None:
    palindromes = set()
    i: int = 1
    while i < MAX:
        if is_dec_pal(i) == True:
            if is_bin_pal(i) == True:
                palindromes.add(i)
        i += 1
    print(sum(palindromes))



##########################################################

if __name__ == "__main__":
    main()

