import random

p = 1 / 3

def g():
    if random.random() < p:
        return 1
    else:
        return 0

# 此算法具有对称性。因此没理由以不同的概率生成 0 / 1
def my_rand():
    while True:
        x = g()
        y = g()
        if x != y:
            return x

one_time = 0
zero_time = 0
for i in range(100000):
    if my_rand() == 1:
        one_time += 1
    else:
        zero_time += 1

print(one_time, zero_time)