def fibonacci(n: int) -> int:
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    n: int = int(input("enter number: "))
    print(f"the {n+1}th term of fibonacci sequence is {fibonacci(n)}.")