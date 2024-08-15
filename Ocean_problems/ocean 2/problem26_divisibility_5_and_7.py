def divisibility(n: int,a: int, b: int) -> int:
    if(n % a == 0) and (n % b == 0):
        return 1
    elif (n % a == 0) or (n % b == 0):
        if n % a == 0:
            return 2
        else:
            return 3
    else:
        return 0

if __name__ == "__main__":
    a: int = 5
    b: int = 7
    n: int = int(input("enter number: "))
    x: int = divisibility(n,a,b)
    if x == 1:
        print(f"{n} is divisible by both {a} & {b}.") 
    elif x == 2:
        print(f"{n} is divisible only by {a}")
    elif x == 3:
        print(f"{n} is divisible only by {b}")
    else:
        print(f"{n} is not divisible by both {a} and {b}")
