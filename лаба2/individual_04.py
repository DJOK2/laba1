import math
import sys

EPSILON = 1e-10
MAX_TERMS = 1000


def sinh_series(x):
    term = x
    total = term
    count = 1
    k = 0

    while abs(term) > EPSILON:
        if count >= MAX_TERMS:
            print("Превышен предел числа членов ряда", file=sys.stderr)
            sys.exit(1)

        term *= x * x / ((2 * k + 2) * (2 * k + 3))
        k += 1
        total += term
        count += 1

    return total, count, abs(term)


def sinh_check(x, terms=50):
    parts = []
    for k in range(terms):
        parts.append(x ** (2 * k + 1) / math.factorial(2 * k + 1))
    return math.fsum(parts)


if __name__ == "__main__":
    x = float(input("Введите x от -1 до 1: "))

    if x < -1 or x > 1:
        print("Недопустимое значение: x должен быть от -1 до 1", file=sys.stderr)
        sys.exit(1)

    result, count, remainder = sinh_series(x)

    print(f"sinh({x}) = {result:.10f}")
    print(f"Членов ряда: {count}")
    print(f"Оценка остатка: {remainder:.3e}")

    check = sinh_check(x)
    print(f"Проверочный расчёт: {check:.10f}")
    print(f"Расхождение: {abs(result - check):.3e}")
    print(f"math.sinh: {math.sinh(x):.10f}")
