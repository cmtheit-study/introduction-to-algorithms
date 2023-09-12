from extended_euclid import extended_euclid

def modular_linear_equation_solver(a: int, b: int, n: int):
    d, x, _ = extended_euclid(a, n)
    if b % d == 0:
        x0 = x * (b // d) % n
        return (x0 + i * n // d for i in range(d))
    else:
        return None

if __name__ == '__main__':
    print(*modular_linear_equation_solver(3, 1, 100))
    print(*modular_linear_equation_solver(35, 10, 50))