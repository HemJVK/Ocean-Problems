# w/o using function
# a: int = int(input("Enter a value for a: "))
# d: int = int(input("Enter a value for d: "))
# b: int = int(input("Enter a value for b: "))

# n: int = b - a
# print("Output: ",a,end = ' ')
# for i in range(n):
#     res: int = a+(i+1)*d
#     if res >= a and res < b  :
#         print(res,end = ' ')
# print()

# using function
def arithmetic_progression(a: int, b: int) -> int:
    n: int = b - a
    res: int = 0
    for i in range(n):
        res = a + (i + 1) * d
        if res>=a and res<b:
            print(res,end = ' ')

if __name__ == "__main__":
    a: int = int(input("Enter a value for a: "))
    d: int = int(input("Enter a value for d: "))
    b: int = int(input("Enter a value for b: "))
    n: int = b - a
    
    print(f"Output: {a}",end=' ')
    arithmetic_progression(a,b)
print()

