import sys


if __name__ == "__main__":
    n = int(input("Введите натуральное число n от 1 до 100000: "))

    if n < 1 or n > 100000:
        print("Недопустимое значение: n должно быть от 1 до 100000", file=sys.stderr)
        sys.exit(1)

    divisors = []
    d = 1
    while d <= n:
        if n % d == 0:
            divisors.append(d)
        d += 1

    print(f"Количество делителей: {len(divisors)}")
    print("Делители:", *divisors)
