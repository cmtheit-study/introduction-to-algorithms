a = [1, 3, 8, 0, 32, 123]

"""
算法执行时间：
T(n) = c1 * n + c2 * n + c3 
     = (c1 + c2) * n + c3
     
故为 n 的一次函数
"""
def search(vec, key):
    # 初始化：搜索过的子数组为空，不包含 key
    for i in range(len(vec)):               # c1    n
        if vec[i] == key:                   # c2    n
            return True                     # c3    1
        # 保持：搜索过的子数组仍然不包含 key
    # 终止：整个数组不包含 key
    return False                            # c3    1

print(search(a, 10), search(a, 8))