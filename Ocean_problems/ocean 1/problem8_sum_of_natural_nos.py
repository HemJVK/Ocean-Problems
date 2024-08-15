def sum_of_natural_nos(n) -> int:
    result: int = 0
    end: int = n + 1
    for i in range(1,end):
        result = result + i
    return result

if __name__ == "__main__":
    n: int = int(input("number: "))
    print(f"the sum of first {n} natural numbers is {sum_of_natural_nos(n)}")