def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Testovací kód
if __name__ == "__main__":
    n = int(input("Zadejte číslo n: "))
    print(f"Fibonacciho číslo pro n={n} je {fib(n)}")
