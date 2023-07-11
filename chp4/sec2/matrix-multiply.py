import numpy as np

def random_two_matrix(
        row = np.random.randint(10, 20),
        m = np.random.randint(10, 20),
        col = np.random.randint(10, 20),
    ):

    return (np.random.randint(low=-256, high=256, size=(row, m)),
            np.random.randint(low=-256, high=256, size=(m, col)))

class MatrixMultiply:
    def __init__(self):
        self.a, self.b = random_two_matrix()
        self.reset_result()

    def reset_result(self):
        self.c = np.zeros(shape=(self.row, self.col))

    @property
    def m(self):
        return self.a.shape[1]

    @property
    def row(self):
        return self.a.shape[0]

    @property
    def col(self):
        return self.b.shape[1]

    def verify(self):
        return all((np.dot(self.a, self.b) == self.c).reshape(self.row * self.col))

    """
    简单矩阵乘法运算
    """
    def simple(self):
        self.reset_result()
        for i in range(self.row):
            for j in range(self.col):
                tot = 0
                for k in range(self.m):
                    tot += self.a[i][k] * self.b[k][j]
                self.c[i][j] = tot

    """
    简单的分治算法
    """
    def div(self):
        n = 1 << np.random.randint(0, 8)
        self.a, self.b = random_two_matrix(n, n, n)
        self.reset_result()
        def rec_div(a, a_row_start, a_row_end, a_col_start, a_col_end,
                    b, b_row_start, b_row_end, b_col_start, b_col_end) -> np.ndarray:
            n = a_row_end - a_row_start + 1
            mid = n >> 1
            c = None
            if a_row_start == a_row_end and a_col_start == a_col_end:
                c = np.ndarray((1, 1))
                c[0][0] = a[a_row_start][a_col_start] * b[b_row_start][b_col_start]
            else:
                a_row_mid = (a_row_start + a_row_end) >> 1
                a_col_mid = (a_col_start + a_col_end) >> 1
                b_row_mid = (b_row_start + b_row_end) >> 1
                b_col_mid = (b_col_start + b_col_end) >> 1

                c11: np.ndarray = \
                    rec_div(a, a_row_start, a_row_mid, a_col_start, a_col_mid,
                            b, b_row_start, b_row_mid, b_col_start, b_col_mid) + \
                    rec_div(a, a_row_start, a_row_mid, a_col_mid + 1, a_col_end,
                            b, b_row_mid + 1, b_row_end, b_col_start, b_col_mid)
                c12: np.ndarray = \
                    rec_div(a, a_row_start, a_row_mid, a_col_start, a_col_mid,
                            b, b_row_start, b_row_mid, b_col_mid + 1, b_col_end) + \
                    rec_div(a, a_row_start, a_row_mid, a_col_mid + 1, a_col_end,
                            b, b_row_mid + 1, b_row_end, b_col_mid + 1, b_col_end)
                c21: np.ndarray = \
                    rec_div(a, a_row_mid + 1, a_row_end, a_col_start, a_col_mid,
                            b, b_row_start, b_row_mid, b_col_start, b_col_mid) + \
                    rec_div(a, a_row_mid + 1, a_row_end, a_col_mid + 1, a_col_end,
                            b, b_row_mid + 1, b_row_end, b_col_start, b_col_mid)
                c22: np.ndarray = \
                    rec_div(a, a_row_mid + 1, a_row_end, a_col_start, a_col_mid,
                            b, b_row_start, b_row_mid, b_col_mid + 1, b_col_end) + \
                    rec_div(a, a_row_mid + 1, a_row_end, a_col_mid + 1, a_col_end,
                            b, b_row_mid + 1, b_row_end, b_col_mid + 1, b_col_end)
                c = np.concatenate(
                    (np.concatenate((c11, c12), axis=1), np.concatenate((c21, c22), axis=1)), axis=0
                )
            return c
        self.c = rec_div(self.a, 0, n - 1, 0, n - 1, self.b, 0, n - 1, 0, n - 1)

if __name__ == '__main__':
    for i in range(10):
        mm = MatrixMultiply()
        mm.div()
        assert mm.verify()