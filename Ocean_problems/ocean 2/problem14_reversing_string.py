def reverse_string(string):
    length: int = len(string)
    reverse: str = ""
    
    for i in range(length-1,-1,-1):
            reverse+=string[i]
    return reverse

if __name__ == "__main__":
    string: str = input()
    print(reverse_string(string))