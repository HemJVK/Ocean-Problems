def prime_no(start, end):
    print(f"prime no from {start} to {end}: ", end="")
    finish: int = end + 1
    for i in range(start, finish):
        flag: bool = False
        for j in range(2, i):
            if i % j == 0:
                flag = True

        if flag == False:
            if i == 1:
                pass
            else:
                print(i, end=" ")


if __name__ == "__main__":
    start: int = int(input("start point: "))
    end: int = int(input("end point: "))
    prime_no(start, end)
    print()

