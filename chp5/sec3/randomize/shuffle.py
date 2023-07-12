import random

def randomize_input(vec: list):
    for i in range(len(vec)):
        swp_idx = random.randint(i, len(vec) - 1)
        vec[i], vec[swp_idx] = vec[swp_idx], vec[i]

vec  = [1, 2, 3, 4, 9, 10, 11]

randomize_input(vec)
print(vec)