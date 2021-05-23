#!/usr/bin/env python3


def main():
    nums = list(range(1, 100+1))
    osszeg_negyzete = sum(nums) ** 2
    negyzetosszeg = 0
    for n in nums:
        negyzetosszeg += n**2
    res = osszeg_negyzete - negyzetosszeg
    print("{0} - {1} = {2}".format(osszeg_negyzete, negyzetosszeg, res))
    

#############################################################################

if __name__ == "__main__":
    main()