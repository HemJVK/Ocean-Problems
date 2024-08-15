def tables(n: int) -> str:
    i: int = 1
    j: int = 10
    res: int
    for k in range(j+1):
        if k>=i and k<=j:
            res = n*k
            print(f"{n}X{k}={res}")
    

if __name__ == "__main__":
    n: int = int(input("number: "))
    print(f"{n} Tables:\n")
    tables(n)