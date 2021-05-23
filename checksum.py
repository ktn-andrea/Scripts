#!/usr/bin/env python3



class CheckSum:
    def __init__(self):
        self.diffs = []
        self.checksum = 0

    def check_lines(self, lines):
        diff = 0
        for line in lines:
            diff = max(line) - min(line)
            self.diffs.append(diff)

    def calc_checksum(self):
        self.checksum = sum(self.diffs)
        return self.checksum

    def __str__(self):
        return "CheckSum: {res}".format(res = str(self.checksum))



def main(): 
    sorok = []
    sor = []
    nums_str = []
    with open("day02.txt", "r") as f:
        for line in f:
            line = line.rstrip("\n")
            nums_str = line.split("\t")
            sor = [int(num) for num in nums_str]   
            sorok.append(sor)
    #print(sorok)

    c = CheckSum()
    c.check_lines(sorok)
    c.calc_checksum()
    print(c)


##################################################    

if __name__ == "__main__":
    main()

