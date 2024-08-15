def palindrome(string: str) -> bool:
    flag: bool = True
    for i in range(len(string)):
        if string[i] != string[len(string) - 1 - i]:
            flag = False
        else:
            continue
    return flag


if __name__ == "__main__":
    string: str = input("input: ")
    print("output: ", end="")
    if palindrome(string) == True:
        print("Palindrome")
    else:
        print("Not palindrome")
