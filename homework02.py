m = int(input("Введите число месяца: "))

if m == 12 or m <= 2:
    print("Зима")
elif m >= 3 and m <= 5:
    print("Весна")
elif m >= 6 and m <= 8:
    print("Лето")
elif m >= 9 and m <= 11:
    print("Осень")
else:
    print("Такого месяца не существует")

