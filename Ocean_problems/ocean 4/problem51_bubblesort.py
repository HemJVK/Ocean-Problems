def bubble_sort(arr: [int], n: int) -> [int]:
    swapped: bool
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            break
    return arr


# def print_arr(arr: [int]):
#     print(arr)


if __name__ == "__main__":
    # size: int = int(input("enter size of list: "))
    arr: [int] = []
    arr: [int] = [10, 7, 8, 9, 1, 5]
    # arr = list(map(int, input("enter the list: ").split()))
    size: int = len(arr)
    bubble_sort(arr, size)
    print(f"sorted list (using bubble sort): {arr}")
    # print_arr(arr)
    print()
