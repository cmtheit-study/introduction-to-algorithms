from select_o import select_o

# 基于顺序统计量的快速排序算法，稳定为 n(log n)
def qsort_select_o(A, p, r):
    if p >= r:
        return
    mid, mid_val = select_o(A, p, r, (r - p) // 2)
    A[mid], A[r] = A[r], A[mid]
    i = p - 1
    for j in range(p, r):
        if A[j] < A[r]:
            i += 1
            A[i], A[j] = A[j], A[i]
    m = i + 1
    A[r], A[m] = A[m], A[r]
    qsort_select_o(A, p, m - 1)
    qsort_select_o(A, m + 1, r)

if __name__ == '__main__':
    import random
    for i in range(100):
        A = set()
        for j in range(0, random.randint(10, 200)):
            A.add(random.randint(10, 20000))
        A = list(A)
        qsort_select_o(A, 0, len(A) - 1)
        for i in range(len(A) - 1):
            assert A[i + 1] > A[i]
