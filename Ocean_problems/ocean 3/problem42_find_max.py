def find_max(number_list: [int]) -> int:
    return max(number_list)

if __name__ == "__main__":
    n: int = int(input("Input:\nEnter number of elements : "))
    number_list: [int] = list(map(int, input("Enter the numbers : ").strip().split()))[:n]
    print(f"\nOutput:\nlargest number: {find_max(number_list)}")