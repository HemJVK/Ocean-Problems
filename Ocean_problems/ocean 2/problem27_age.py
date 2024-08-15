def Age(age: int) -> str:
    if(age < 18):
        return "You are a minor." 
    elif(age >= 18) and (age <= 65):
        return "You are an adult."
    else:
        return "You are a senior citizen."

if __name__ == "__main__":
    age: int = int(input("Enter your age: "))
    condition: str = Age(age)
    print(condition)

    