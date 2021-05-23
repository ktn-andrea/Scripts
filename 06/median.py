#!/usr/bin/env python3


def test(li):
    li.sort()
    middle = len(li) // 2
    if len(li) % 2 == 0:
        median = (li[middle] + li[middle-1]) / 2
    else:
        median = li[middle]
    return median



def main():
    print("median of [1, 2, 3, 4, 5] --> ", test([1, 2, 3, 4, 5]))
    print("median of [3, 1, 2, 5, 3] --> ", test([3, 1, 2, 5, 3]))
    print("median of [1, 300, 2, 200, 1] --> ", test([1, 300, 2, 200, 1]))
    print("median of [3, 6, 20, 99, 10, 15] --> ", test([3, 6, 20, 99, 10, 15]))
    
    


#############################################################################

if __name__ == '__main__':
    main()
