def spiral(lim: int) -> str:
    string: str = "".join(
        f"{'R' * (2 * i - 1) + 'U' * (2 * i - 1) + 'L' * (2 * i) + 'D' * (2 * i)}"
        for i in range(lim)
    )
    return string


def write_in_text_file(lim: int):
    with open("spiral.txt", "w") as f:
        f.write("spiral:\n\t" + spiral(lim) + "\n\n")
        f.write(f"count: {len(spiral(lim))}")


if __name__ == "__main__":
    # num: int = int(input("enter the number of times the spiral should iterate: "))
    num: int = 501
    string: str = spiral(num)
    print("spiral:\n\t", end="")
    print(string)
    print(f"\ncount: {len(string)}")
    write_in_text_file(num)
