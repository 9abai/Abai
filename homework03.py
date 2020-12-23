m = int(input("Введите месяц: "))
d = int(input("Введите день: "))

if (d >= 21 and m == 3) or (m == 4 and d < 21):
    print("Овен")
elif (d >= 21 and m == 4) or (m == 5 and d < 21):
    print("Телец")
elif (d >= 21 and m == 5) or (m == 6 and d < 21):
    print("Близнецы")
elif (d >= 21 and m == 6) or (m == 7 and d < 21):
    print("Рак")
elif (d >= 21 and m == 7) or (m == 8 and d < 21):
    print("Лев")
elif (d >= 21 and m == 8) or (m == 9 and d < 21):
    print("Дева")
elif (d >= 21 and m == 9) or (m == 10 and d < 21):
    print("Весы")
elif (d >= 21 and m == 10) or (m == 11 and d < 21):
    print("Скорпион")
elif (d >= 21 and m == 11) or (m == 12 and d < 21):
    print("Стрелец")
elif (d >= 21 and m == 12) or (m == 1 and d < 21):
    print("Козерог")
elif (d >= 21 and m == 1) or (m == 2 and d < 21):
    print("Водолей")
elif (d >= 21 and m == 2) or (m == 3 and d < 21):
    print("Рыбы")