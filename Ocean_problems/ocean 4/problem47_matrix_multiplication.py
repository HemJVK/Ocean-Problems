# matrix multiplication works only for matrices with same dimensions


def matrix_multiplication(r: int, c: int, mat1: list[list[int]], mat2: list[list[int]]):
    product: list[list[int]] = mat1

    for i in range(r):
        for j in range(c):
            for k in range(c):
                product[i][j] = mat1[i][k] * mat2[k][j]

    for i in range(r):
        for j in range(c):
            print(product[i][j], end=" ")
        print()


if __name__ == "__main__":
    r: int = int(input("enter rows: "))
    c: int = int(input("enter columns: "))
    print("enter matrix 1:")
    mat1: list[list[int]] = [[int(input()) for j in range(r)] for i in range(c)]
    print("enter matrix 2:")
    mat2: list[list[int]] = [[int(input()) for j in range(c)] for i in range(r)]

    print("product of matrices:\n")

    matrix_multiplication(r, c, mat1, mat2)
