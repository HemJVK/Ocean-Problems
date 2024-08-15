def merge(arr: [int], left: int, mid: int, right: int) -> [int]:
    sub_arr1: int = mid - left + 1
    sub_arr2: int = right - mid

    L: [int] = [0] * sub_arr1  # Initialize L with zeros
    R: [int] = [0] * sub_arr2  # Initialize R with zeros

    for i in range(sub_arr1):
        L[i] = arr[left + i]
    for j in range(sub_arr2):
        R[j] = arr[mid + 1 + j]

    i, j, k = 0, 0, left
    while i < sub_arr1 and j < sub_arr2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < sub_arr1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < sub_arr2:
        arr[k] = R[j]
        j += 1
        k += 1

    return arr


# Example usage:
# arr = [38, 27, 43, 3, 9, 82, 10]
# merge(arr, 0, 2, 6)
# print(arr)


def merge_sort(arr: [int], left: int, right: int):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


# def print_arr(arr: [int]):
#     print(arr)


if __name__ == "__main__":
    # size: int = int(input("enter array size: "))
    # arr: [int] = [10,7,8,9,1,5]
    arr: [int] = list(map(int, input("enter the list: ").split()))
    size: int = len(arr)
    merge_sort(arr, 0, size - 1)
    print(f"sorted array (using merge sort): {arr}")
    # print_arr(arr)
