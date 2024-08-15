def power(n: int) -> (int, int, int):
    square: int = pow(n,2)
    cube: int = pow(n,3)
    pow_n: int = pow(n,n)
    return square,cube,pow_n 

if __name__ == "__main__":
    n: int = int(input("enter no: "))
    square, cube, pow_n = power(n)
    
    print(f"the square, cube and power n of {n} is: {square}, {cube}, {pow_n}")