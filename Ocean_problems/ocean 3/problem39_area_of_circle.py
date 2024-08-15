import math
PI = math.pi
def circle_area(radius: float):
    return PI*pow(radius,2)

if __name__ == "__main__":
    radius: float = float(input("radius: ")) 
    print(f"area of circle of radius {radius}: {circle_area(radius):.3f}")