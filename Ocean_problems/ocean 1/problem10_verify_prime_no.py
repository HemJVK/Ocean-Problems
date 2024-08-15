def verify_prime(n) -> str:
    if n > 1:
        for i  in range(2,n-1):
            if(n % i) == 0:
                return f"{n} is not a Prime number"
                break
        else:
            return (f"{n} is a Prime number")
    else:
        return (f"{n} is not a natural number")


if __name__ == "__main__":
    n: int = int(input("number: "))
    print(verify_prime(n))
    
    

    
