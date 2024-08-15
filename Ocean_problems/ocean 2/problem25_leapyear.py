def leap_year_not(year: int) -> str:
        if(year % 100 == 0) and (year % 400 == 0):
                return "a Leap Yr"
        elif(year % 100 != 0) and (year % 4 == 0):
                return "a leap yr"
        else:
                return "not a leap yr"

if __name__ == "__main__":
        print("Input:")
        year: int = int(input("Enter year: "))
        print(f"\nOutput:\n{year} is {leap_year_not(year)}")
