def right_angled_triangle(n: int) -> int:
    for i in range(n+1):
        print('*'*i)

if __name__ == "__main__":
    n: int = int(input("enter number: "))
    right_angled_triangle(n)