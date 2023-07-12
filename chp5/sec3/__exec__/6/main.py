import random

def randomize_input(vec: list):
    p = []
    for v in vec:
        p.append((v, random.randint(0, len(vec) ** 2)))
    p.sort(key=lambda t: t[1])
    last_same_weighted = None
    for idx, (v, w) in enumerate(p):
        if last_same_weighted != w:
            same_weighted = list(v for v, w in filter(lambda m: m[1] == w, p))
            if len(same_weighted) > 1:
                last_same_weighted = w
                randomize_input(same_weighted)  # 对于相同权重者，递归调用算法
            vec[idx:(idx + len(same_weighted))] = same_weighted[:]


for i in range(100000):
    vec = [1, 3, 4, 5, 6, 9, 10]
    cs = set(vec)
    randomize_input(vec)
    assert cs == set(vec)