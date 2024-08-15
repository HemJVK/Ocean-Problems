def concatenate(string1: str, string2: str) -> str:
    return f"{string1} {string2}"

if __name__ == "__main__":
    string1: str = input("string1: ")
    string2: str = input("string2: ")
    
    print(f"concatenated strings: {concatenate(string1,string2)}")
    