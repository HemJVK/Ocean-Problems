def factorial(n: int) -> int:
    if n in {0,1}:
        return 1
    elif n >= 1000:
        var: int = 1
        for i in range(1,n+1):
            var *= i
        return var
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    n: int = int(input("enter number: "))
    x: int = factorial(n)
    if len(str(x)) <= 5:
        print(f"factorial of {n} is {x}")
    else:
        print(f"factorial of {n} is 10^{len(str(x))}")
    