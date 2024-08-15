def partition(arr: [int], low: int, high: int):
    pivot: int = arr[high]
    i: int = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr: [int], low: int, high: int):
    if low < high:
        pi: int = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


if __name__ == "__main__":
    # arr: [int] = list(map(int, input("Enter the list: ").split(",")))
    arr: [int] = [10, 7, 8, 9, 1, 5]
    n: int = len(arr)
    quick_sort(arr, 0, n - 1)
    print(f"sorted list (using quick sort): {arr}")
