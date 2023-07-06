a = [1, 0, 0, 0, 1]
b = [0, 0, 1, 1, 1]

"""
a   b   c   Res C
0   0   0   0
0   0   1   1
0   1   0   1
0   1   1   
1   0   0
1   0   1
1   1   0
1   1   1
"""

def bin_add(vec1, vec2):
    carry = 0
    c = []
    # 初始化：未有相加结果
    for i in range(1, len(vec1) + 1):
        cnt = 0
        if a[-i]: cnt += 1
        if b[-i]: cnt += 1
        if carry: cnt += 1
        res = cnt & 1
        carry = (cnt & 2) >> 1
        c.insert(0, res)
        # 保持：右侧的位被正确相加，进位正确设置
    # 终止：所有位数被正确相加，进位都正确设置
    c.insert(carry, 0)
    # 算法终止：进位插入，结果算出
    return c

print(bin_add(a, b))
