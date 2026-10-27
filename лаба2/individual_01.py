import sys


def daily_pay(kg):
    if kg <= 50:
        rate = 30
    elif kg <= 75:
        rate = 50
    elif kg <= 90:
        rate = 65
    else:
        rate = 70

    bonus = 20 if kg > 90 else 0
    return kg * rate / 100 + bonus


if __name__ == "__main__":
    x = float(input("Введите вес собранных помидоров, кг: "))

    if x < 0 or x > 1000:
        print("Недопустимое значение: вес должен быть от 0 до 1000 кг", file=sys.stderr)
        sys.exit(1)

    print(f"Заработок за день: {daily_pay(x):.2f} руб.")
