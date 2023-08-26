# A 和 B 都为升序，且长度相同
def ordered_mid(A: list[int], B: list[int]):
    n = len(A)
    a_low = 0
    a_high = n - 1
    while a_high > a_low:
        a_mid = (a_low + a_high) // 2
        b_mid = n - a_mid - 1
        if A[a_mid] < B[b_mid]:
            if b_mid != 0 and A[a_mid] > B[b_mid - 1] or b_mid == 0:
                return A[a_mid]
            a_low = a_mid + 1
        elif A[a_mid] > B[b_mid]:
            if a_mid != 0 and B[b_mid] > A[a_mid - 1] or a_mid == 0:
                return B[b_mid]
            a_high = a_mid
        else:
            return A[a_mid]
    else:
        a_mid = (a_low + a_high) // 2
        b_mid = n - a_mid - 1
        return min(A[a_mid], B[b_mid])

if __name__ == '__main__':
    from random import randint
    from timeit import *
    i = 1
    while i <= 10000000:
        A = []
        B = []
        for j in range(i):
            A.append((A[j - 1] if j else 0) + randint(0, 200))
            B.append((B[j - 1] if j else 0) + randint(0, 200))
        timer = timeit('ordered_mid(A, B)', globals={
            'ordered_mid': ordered_mid,
            'A': A,
            'B': B
        })
        print(i, '耗时：', timer * 1000, ' ms')
        i *= 10
