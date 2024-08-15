def concatenation(string1: str, string2: str):
    return(string1 + string2)

if __name__ == "__main__":
    str1: str = input("enter string1: ")
    str2: str = input("enter string2: ")

    print(f"concatenation of {str1} & {str2} is {concatenation(str1,str2)}")