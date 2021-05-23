#!/usr/bin/env python3


def open_door(li, begin):
    for i in range(1, len(li)+1):
        if i % begin == 0:
            li[i-1] = rotate_key(li[i-1])
    return li


def rotate_key(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0


def main(): 
    doors = [0 for i in range(1, 600+1)]

    for d in range(1, len(doors)+1):
        doors = open_door(doors, d)

    res = []
    for i in range(1, len(doors)+1):
        if doors[i-1] == 1:
            res.append(i)

    print("Nyitott ajtok sorszamai: ")
    print(res)
    print(''.join([str(i) for i in res]))
    


#######################################################

if __name__ == "__main__":
    main()
