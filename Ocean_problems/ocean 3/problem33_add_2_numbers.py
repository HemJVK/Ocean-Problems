def add(a: int, b: int) -> int:
    return a+b

if __name__ == "__main__":
    a: int = int(input("enter 1st number: "))
    b: int = int(input("enter 2nd number: "))
    print(f"the sum of {a} & {b} is {add(a,b)}.")
    