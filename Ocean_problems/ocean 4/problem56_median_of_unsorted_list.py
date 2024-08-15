def median(l: [int]):
    sum: int = 0
    avg: int = 0
    for i in range(len(l)):
        sum += l[i]
    avg = sum // len(l)
    return avg


if __name__ == "__main__":
    # num: [int] = [10, 7, 8, 9, 1, 5]
    # num: int = [1, 2, 3, 4, 5]
    # num: [int] = list(map(int, input("enter the list: ").split(",")))
    print(f"the median is: {median(num)}")
