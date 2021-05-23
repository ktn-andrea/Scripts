#!/usr/bin/env python3


def ex_2():
    """Capitalizes the words of a given list."""
    words = ['aladar', 'bela', 'cecil']
    result = [w.capitalize() for w in words]
    print("2.feladat")
    print(words)
    print(result)


def ex_8():
    """Selects the first letters of words in a given list."""
    sentence = "python is an awesome language"
    result = [w[0] for w in sentence.split()]
    print("8.feladat")
    print(sentence)
    print(result)


def ex_9():
    """Collects the words and their lenghts of a list in a list of tuples."""
    sentence = 'The quick brown fox jumps over the lazy dog'
    result = [(w, len(w)) for w in sentence.split()]
    print("9.feladat")
    print(sentence)
    print(result)


def ex_10():
    """Creates even numbers less that 10."""
    result = list(range(0, 10, 2))
    print("10.feladat")
    print(result)


def ex_11():
    """Squares numbers less than 20 and selects the even ones."""
    nums = list(range(0, 20))
    result = [n*n for n in nums if (n*n)%2 == 0]
    print("11.feladat")
    print(result)


def ex_12():
    """Squares numbers less than 20 and selects those that end with 4."""
    nums = list(range(0, 20))
    result = [n*n for n in nums if str(n*n)[-1] == '4']
    print("12.feladat")
    print(result)


def ex_13():
    """Creates the letters of the alphabet."""
    letters = [chr(i) for i in range(65, 90+1)]
    result = ''.join(letters) 
    print("13.feladat")
    print(letters)
    print(result)


def ex_14():
    """Removes whitespace from beginning and end of words in a list."""
    words = [' apple ', ' banana ', ' kiwi']
    result = [w.strip() for w in words]
    print("14.feladat")
    print(words)
    print(result)


def ex_15():
    """Creates string from list of numbers."""
    nums = [1, 0, 1, 1, 0, 1, 0, 0]
    result = ''.join([str(n) for n in nums])
    print("15.feladat")
    print(nums)
    print(result)



def main(): 
    ex_2()
    print("-" *40)
    ex_8()
    print("-" *40)
    ex_9()
    print("-" *40)
    ex_10()
    print("-" *40)
    ex_11()
    print("-" *40)
    ex_12()
    print("-" *40)
    ex_13()
    print("-" *40)
    ex_14()
    print("-" *40)
    ex_15()



if __name__ == "__main__":
    main()

