a = [3, 1, 10, 8, 323, -12, 32, 0]

"""
复杂度分析
T(n) = (c1 + c2 + c6) * n + (c3 + c4 + c5) * (n - 1 + 2) * (n - 1 - 1) / 2
     = (c1 + c2 + c6) * n + (c3 + c4 + c5) * (n ** 2 - n - 2) / 2
     = (c3 + c4 + c5) * n ** 2 / 2 + (c1 + c2 + c6 - (c3 + c4 + c5) / 2) * n - (c3 + c4 + c5) 
O(n**2)
"""
def select_sort(vec):
    # 初始化：数组前 0 个是有序的
    for i in range(len(a) - 1):                         # c1    n
        smallest = i                                    # c2    n
        for j in range(i + 1, len(a)):                  # c3    (n - 1) + (n - 2) + ... + 2
            if vec[j] < vec[smallest]:                  # c4    up
                smallest = j                            # c5    up
        vec[i], vec[smallest] = vec[smallest], vec[i]   # c6    n
        # 保持：数组前 i + 1 个是有序的
    # 终止：数组前 len(a) - 1 个是有序的
    # 算法终止：数组最后一个是最大的。所以整个数组都是有序的
select_sort(a)
print(a)
