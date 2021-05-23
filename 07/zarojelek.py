#!/usr/bin/env python3


OPENING = ["(","[","{"]
CLOSING = [")","]","}"]


def test(expression):
    li = []
    for i in expression:
        if i in OPENING:
            li.append(i)
        elif i in CLOSING:
            pos = CLOSING.index(i)
            if (len(li) > 0) and (OPENING[pos] == li[len(li)-1]):
                li.pop()
            else:
                return False
    return len(li) == 0



def main(): 
    print("((5+3)*2+1) --> ", test("((5+3)*2+1)"))
    print("{[(3+1)+2]+} --> ", test("{[(3+1)+2]+}"))
    print("(3+{1-1)} --> ", test("((3+{1-1)}"))
    print("[1+1]+(2*2)-{3/3} --> ", test("[1+1]+(2*2)-{3/3}"))
    print("(({[(((1)-2)+3)-3]/3}-3) --> ", test("(({[(((1)-2)+3)-3]/3}-3)"))


if __name__ == "__main__":
    main()

