import random

v = []
for i in range(100):
    v.append(random.randint(-200, 200))

def merge(vec: list, a, m, b):
    l1 = vec[a:m]
    l2 = vec[m:b]
    # 初始化：已插入的序列长度为 0，自然有序
    for i in range(a, b):
        if not l1:
            vec[i:b] = l2[:]
            break
        elif not l2:
            vec[i:b] = l1[:]
            break
        else:
            if l1[0] > l2[0]:
                vec[i] = l2[0]
                l2.pop(0)
            else:
                vec[i] = l1[0]
                l1.pop(0)
        # 保持：从 [a, a + i] 范围内有序
    # 终止：vec 的 [a, b] 范围内有序
    # 算法终止：实现 merge 两个有序子序列的功能

"""
算法分析
T(b - a) = T(m - a) + T(b - m) + b - a
设 n = b - a，已知 m = (a + b) // 2 
则 T(n) ≈ 2 * T(n // 2) + n  
        =  
"""
def sort(vec: list, a, b):      # T(b - a)
    if a < b - 1:
        m = (a + b) // 2
        sort(vec, a, m)         # T(m - a)  1
        sort(vec, m, b)         # T(b - m)  1
        merge(vec, a, m, b)     # b - a     1

sort(v, 0, len(v))
print(v)