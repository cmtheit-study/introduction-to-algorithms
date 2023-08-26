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
def randomized_select(A, i):
    high = len(A) - 1
    low = 0
    while high > low:
        q = randomized_partition(A, low, high)
        k = q - low
        if k > i:
            high = q - 1
        elif k < i:
            low = q + 1
            i -= k + 1
        else:
            return A[q]
    return A[low]

A = [1, 2, 3, 4, 5, -1, 1000, -32, -4, 0]
print(randomized_select(A, 3))

if __name__ == '__main__':
    import random
    for i in range(1000):
        l = random.randint(10, 100)
        A = []
        for i in range(l):
            A.append(random.randint(100, 1000))
            j = random.randint(0, len(A) - 1)
            v = randomized_select(A, j)
            A.sort()
            assert A[j] == v, (v, j)