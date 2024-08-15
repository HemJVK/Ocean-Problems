def natural_no(n: int) -> [int]:
    natural: [int] = list(range(1,n+1))
    return natural

if __name__ == "__main__":
    n: int = int(input("enter no of terms: "))
    print(f"the list of {n} natural numbers are: {natural_no(n)}")
    