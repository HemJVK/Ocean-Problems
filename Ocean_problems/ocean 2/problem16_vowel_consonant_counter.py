vowels = ['a', 'e', 'i', 'o', 'u']
# symbols = ['.',',','','"',"'"]

def counter(string: str) -> (int,int):
    j: int = 0
    count_vowel: int = 0
    count_consonant: int = 0
    for i in range(len(string)):
        if(string[i].isalpha()):
            if(string[i] in vowels):
                count_vowel += 1
            else:
                count_consonant += 1
    return count_vowel, count_consonant
    

if __name__ == "__main__":
    string: str = input("enter string: ")
    vowel, consonant = counter(string)
    print(f"vowel count: {vowel}\nconsonant count: {consonant}")