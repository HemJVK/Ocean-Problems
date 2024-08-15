def str_intersparse (string1, string2) -> str:
    result: str = ""
    length: int = min(len(string1),len(string2))
    for i in range(length):
        result += string1[i] + string2[i]
    i += 1
    if (len(string1) == length):
        while (i < len(string2)):
            result += string2[i]
            i += 1
    else:
        while (i < len(string1)):
            result += string1[i]
            i += 1
    return result

if __name__ == "__main__":
    print("Input:")
    string1: str = input() 
    string2: str = input()
    print(f"Output:\n{str_intersparse(string1, string2)}")