#!/usr/bin/env python3



def prime_palindrome(num: int) -> int:
    if num <= 1:
        return 2
    elif num == 2:
        return 3

    n: int = num
    is_prime: bool = True
    while True:
        n += 1
        for j in range(2, n):
            if n % j == 0:
                is_prime = False
                break
            else:
                is_prime = True
        if is_prime == True and n > num:
            if str(n) == str(n)[::-1]:
                return int(n)
        

    
def main() -> None: 
    print(prime_palindrome(31) == 101)
    print(prime_palindrome(130) == 101)
    print(prime_palindrome(131) == 101)
    print(prime_palindrome(1977) == 101)
    
    n:int = int(input("Adjon meg egy szamot: "))
    m:int = prime_palindrome(n)
    print("{N}-nel nagyobb prim palindrom: {M}".format(N=n, M=m))

    





if __name__ == "__main__":
    main()

