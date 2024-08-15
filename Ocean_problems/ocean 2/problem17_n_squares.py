def squares(n: int)-> int:
    square: int = []
    for i in range(1,n+1):
        square.append(pow(i,2))
    return square 

if __name__ == "__main__":
    n: int = int(input("enter number: "))
    print(f"the square of first {n} is: ",end = '')
    print(squares(n),end=' ')

print()