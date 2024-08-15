def temperature_converter(temperature: int,choice: int) -> int:
    if choice == 1:
        return (int)((temperature * (5/9)) + 32)
    elif choice == 2:
        return (int)((temperature - 32) * (9/5))

if __name__ == "__main__":
    degree = u"\N{DEGREE SIGN}"
    choices: int = int(input(f"choices:\n1.{degree}C to {degree}F\n2.{degree}F to {degree}C\nEnter your choice: "))
    if choices == 1:
        temperature: int = int(input(f"enter temperature in {degree}C: "))
        print(f"the temperature {temperature}{degree}C has been converted to {temperature_converter(temperature, choices)}{degree}F.")
    elif choices == 2:
        temperature: int = int(input(f"enter temperature in {degree}F: "))
        print(f"the temperature {temperature}{degree}F has been converted to {temperature_converter(temperature, choices)}{degree}C.")
    else:
        print("error!! choice not found!!!")
        
        
        