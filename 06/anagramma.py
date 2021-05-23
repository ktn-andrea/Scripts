#!/usr/bin/env python3



def normalize(word):
    return word.replace(' ', '').lower()


def anagramma_1(word_1, word_2):
    if len(word_1) != len(word_2):
        return False
    for i in word_1:
        if i in word_2:
            continue
        else:
            return False
    return True


def anagramma_2(word_1, word_2):
    if sorted(word_1) == sorted(word_2):
        return True
    return False


def main():
    szo_1 = normalize(input("Elso szo: "))
    szo_2 = normalize(input("Masodik szo: "))

    print("\"{0}\" és \"{1}\" anagramma: {2}".format(szo_1, szo_2, anagramma_1(szo_1, szo_2)))



#############################################################################

if __name__ == '__main__':
    main()
