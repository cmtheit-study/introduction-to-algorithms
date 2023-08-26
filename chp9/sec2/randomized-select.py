# 期望时间为线性的算法

def randomized_partition(A, p, r):
    from random import randint
    if p == r:
        return p
    i = randint(p, r)
    A[i], A[r] = A[r], A[i]
    m = p - 1
    for n in range(p, r):
        if A[n] <= A[r]:
            m += 1
            A[m], A[n] = A[n], A[m]
    A[r], A[m + 1] = A[m + 1], A[r]
    return m + 1

# 顺序统计量
def randomized_select(A, p, r, i):
    if p == r:
        return A[p]
    q = randomized_partition(A, p, r)
    k = q - p
    if k > i:
        return randomized_select(A, p, q - 1, i)
    elif k < i:
        return randomized_select(A, q + 1, r, i - k - 1)
    else:
        return A[q]

A = [1, 2, 3, 4, 5, -1, 1000, -32, -4, 0]
print(randomized_select(A, 0, len(A) - 1, 3))

if __name__ == '__main__':
    import random
    for i in range(1000):
        l = random.randint(10, 100)
        A = []
        for i in range(l):
            A.append(random.randint(100, 1000))
            j = random.randint(0, len(A) - 1)
            v = randomized_select(A, 0, len(A) - 1, j)
            A.sort()
            assert A[j] == v, (v, j)