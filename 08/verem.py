#!/usr/bin/env python3



class Verem():
    def __init__(self):
        self.tartalom = [] 

    def ures(self):
        return len(self.tartalom) == 0

    def meret(self):
        return len(self.tartalom)

    def betesz(self, elem):
        self.tartalom.append(elem)

    def kivesz(self):
        if self.ures():
            return None
        return self.tartalom.pop()

    def __str__(self):
        if self.ures():
            return '['
        return '[' + ' '.join(str(li) for li in self.tartalom)




def main(): 
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)








if __name__ == "__main__":
    main()

