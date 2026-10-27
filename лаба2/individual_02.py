import sys


if __name__ == "__main__":
    x = int(input("Введите натуральное число x: "))
    y = int(input("Введите натуральное число y: "))

    if x < 1 or y < 1:
        print("Недопустимое значение: числа должны быть натуральными", file=sys.stderr)
        sys.exit(1)

    remainder = x % y

    if remainder == 0:
        print(f"Число {x} делится на {y} нацело, частное: {x // y}")
    else:
        print(f"Число {x} не делится на {y} нацело, остаток: {remainder}")
