import math

def decimal_2_binary_converter(decimal_no: int) -> str:
    binary_number: str = ""
    while decimal_no >=1:
        binary_number = str(math.floor(decimal_no % (2))) + binary_number
        decimal_no/=2
        
    return binary_number

if __name__ == "__main__":
    decimal_no: int = int(input("Enter the Decimal Number: "))
    print(decimal_2_binary_converter(decimal_no))
    # binary = map(decimal_2_binary_converter(decimal_no),len(decimal_2_binary_converter(decimal_no)))
    # print(f"the Binary representation of {decimal_no} is {binary} ")