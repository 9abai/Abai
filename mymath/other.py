def around():
    z = float(input("Введите не целое число: "))
    print(round(z))

def miv():#min value
    spisok = []
    x = input("Введите первое значене: ")
    y = input("Введите второе значение: ")
    z = input("Введите третье значение: ")
    spisok.append(x)
    spisok.append(y)
    spisok.append(z)
    print(min(spisok))
def mav():#max value
    spisok = []
    x = input("Введите первое значене: ")
    y = input("Введите второе значение: ")
    z = input("Введите третье значение: ")
    spisok.append(x)
    spisok.append(y)
    spisok.append(z)
    print(max(spisok))