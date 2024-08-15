def fibonacci_series(n: int) -> int:
    return n if n <= 1 else fibonacci_series(n-1) + fibonacci_series(n-2)
        
    


if __name__ == "__main__":
    n: int = int(input("number: "))
    print("Fibonacci Series: ",end='')
    for i in range(n):
        print(fibonacci_series(i),end=' ')
    print()

