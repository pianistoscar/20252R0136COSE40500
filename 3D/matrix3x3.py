class Matrix3x3:
    def __init__(self, data):
        self.data = data  # 3x3 list

    def multiply(self, other):
        result = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix3x3(result)


if __name__ == "__main__":
    A = Matrix3x3([[1, 0, 0],
                   [0, 1, 0],
                   [0, 0, 1]])

    B = Matrix3x3([[2, 1, 0],
                   [0, 1, 0],
                   [0, 0, 1]])

    C = A.multiply(B)
    print(C.data)
