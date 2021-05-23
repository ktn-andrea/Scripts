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


class MyQueue:
    def __init__(self):
        self.v1 = Verem()
        self.v2 = Verem()

    def append(self, value):
        self.v1.betesz(value)

    def popleft(self):
        for i in self.v1.tartalom[::-1]:
            self.v2.betesz(i)
            self.v1.kivesz()
        self.v2.kivesz()
        for i in self.v2.tartalom[::-1]:
            self.v1.betesz(i)
            self.v2.kivesz()
        return self.v1.tartalom

    def is_empty(self):
        return self.v1.ures()

    def size(self):
        return self.v1.meret()

    def __str__(self):
        return self.v1.__str__()


def main():
    q = MyQueue()
    q.append(62)
    q.append(78)
    q.append(51)
    print(q)
    print(q.is_empty())
    print(q.size())
    q.append(93)
    print(q)
    print(q.size())
    q.popleft()
    print(q)
    q.popleft()
    print(q)
    q.popleft()
    print(q)
    print(q.is_empty())
    q.popleft()
    print(q)
    print(q.size())
    print(q.is_empty())
    

##################################

if __name__ == "__main__":
    main()