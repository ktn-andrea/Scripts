#!/usr/bin/env python3


import re

PATTERN = '.*j.*s.*u.*n.*'


def search_words(text) -> str():
    li = [line.split(',')[0] for line in text]
    res = []
    for word in li:
        act = re.search(PATTERN, word)
        if act:
            res.append(word)
    return res
        

def main(): 
    f = open("corpus.txt", "r")
    lines = f.read().splitlines()
    f.close()

    print(search_words(lines))

    


###################################################################

if __name__ == "__main__":
    main()
