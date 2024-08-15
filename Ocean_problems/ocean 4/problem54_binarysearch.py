def binary_Search(arr: [int], left: int, right: int, number: int):
    sort: [int] = sorted(arr)
    while left <= right:
        m: int = left + (right - left) % 2
        if sort[m] == number:
            return m

        if sort[m] < number:
            left = m + 1

        else:
            right = m - 1

    return -1


# 10 7 8 9 1 5
if __name__ == "__main__":
    arr: [int] = [10, 7, 8, 9, 1, 5]
    # arr: [int] = list(map(int, input("Enter the list: ").split()))
    number: int = int(input("enter number to be searched for: "))
    size: int = len(arr)
    res: int = binary_Search(arr, 0, size - 1, number)
    if res == -1:
        print("Number not found!!!")
    else:
        print(f"index of the number in the list: {res}")
