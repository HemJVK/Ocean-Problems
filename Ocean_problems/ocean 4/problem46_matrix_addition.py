def matrix_addition(n: int, mat1: list[list[int]], mat2: list[list[int]]):
    add: list[list[int]] = mat1
    for i in range(n):
        for j in range(n):
            add[i][j] = mat1[i][j] + mat2[i][j]
    for i in range(n):
        for j in range(n):
            print(add[i][j], end="  ")
        print()


if __name__ == "__main__":
    n: int = int(input("enter dimension of matrix: "))
    print("enter 1st matrix:")
    mat1: list[list[int]] = [[int(input()) for j in range(n)] for i in range(n)]
    print("enter 2nd matrix:")
    mat2: list[list[int]] = [[int(input()) for j in range(n)] for i in range(n)]

    print("the sum of the matrices is:")
    matrix_addition(n, mat1, mat2)
