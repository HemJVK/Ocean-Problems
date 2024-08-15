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
    print(f"the factorial of {n} is {factorial(n)}")
