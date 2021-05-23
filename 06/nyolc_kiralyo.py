#!/usr/bin/env python3



def draw(positions):
    print("+" + "-"*26 + "+")
    for i in range(7, -1, -1):
        row = "| "
        for j in positions:
            if i == j:
                row += " Q "
            else:
                row += " . "
        print(row + " |")
    print("+" + "-"*26 + "+")
    


def main():
    draw([7,3,0,2,5,1,6,4])
    draw([0,4,7,5,2,6,1,3])
    



#############################################################################

if __name__ == '__main__':
    main()
