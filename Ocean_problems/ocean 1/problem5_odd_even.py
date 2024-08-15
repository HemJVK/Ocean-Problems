def odd_even(n: int) -> str:
    if(n % 2 == 0):
        return "even"
    else:
        return "odd"
    
if __name__ == "__main__":
    n: int = int(input("number: "))
    print(odd_even(n))