def write_in_text_file(n: int):
    with open("output.txt", "w") as f:
        for i in range(n):
            f.write(str(i + 1))


if __name__ == "__main__":
    n: int = int(input("size: "))
    for i in range(n):
        print(i + 1)
    write_in_text_file(n)
