def type_of_sign(n: int):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    else:
        return 1


if __name__ == "__main__":
    n: int = int(input("enter no: "))
    sign: int = type_of_sign(n)
    if sign == -1:
        print(f"{n} is Negative")
    elif sign == 0:
        print("Zero")
    else:
        print(f"{n} is Positive")