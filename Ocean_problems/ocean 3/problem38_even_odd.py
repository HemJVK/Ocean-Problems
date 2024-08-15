def is_even(number: int) -> bool:
    return number != 0 and number % 2 == 0
    
if __name__ == "__main__":
    number: int = int(input("Input: "))
    if(is_even(number) == True):
        print(f"Output:\nsince it's {is_even(number)}, {number} is Even")
    elif(number == 0):
        print(f"Output:\nsince it's {is_even(number)}, {number} neither even nor odd")
    else:
        print(f"Output:\nsince it's {is_even(number)}, {number} is Odd")    