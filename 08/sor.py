#!/usr/bin/env python3



class Sor():
    def __init__(self):
        self.tartalom = []

    def enqueue(self, elem):
        self.tartalom.append(elem)

    def peek(self):
        if self.is_empty == True:
            return None
        return self.tartalom[0]

    def count(self):
        return len(self.tartalom)

    def clear(self):
        self.tartalom = []

    def is_empty(self):
        return len(self.tartalom) == 0

    def dequeue(self):
        if self.is_empty == True:
            return None
        return self.tartalom.pop(0)

    def __str__(self):
        if self.is_empty():
            return '['
        return '[' + ' '.join(str(li) for li in self.tartalom)




def main(): 
    s = Sor()
    print(s)
    print(s.is_empty()) 
    s.enqueue(43)
    s.enqueue(54)
    s.enqueue(13)
    s.enqueue(98)
    s.enqueue(22)
    print(s)
    print(s.count())
    print(s.is_empty())
    print(s.peek())
    s.dequeue()
    s.dequeue()
    x = s.dequeue()
    print("x:", x)
    print("s: ",s) 
    x = s
    print("x:", x)
    print(s.peek())
    s.clear()
    print(s.is_empty())
    







if __name__ == "__main__":
    main()

