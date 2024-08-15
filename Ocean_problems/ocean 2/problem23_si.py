def simple_interest(principle: float, rate: float, time: float) -> float:
    si: float = principle*rate*time
    return si

if __name__ == "__main__":
    principle: float = float(input("enter principle: "))
    rate: float = float(input("enter rate: "))
    time: float = float(input("enter time: "))

    print(f"simple interest: ${simple_interest(principle,rate,time)}")
    