names = []
m = []
f = []

while len(names) < 5:
    name = input("Введите имя: ")
    g =  input("их гендер (m/f): ")
    if g == "m":
        m.append(name)
    elif g == 'f':
        f.append(name)
    else:
        print("такого значения не существует")
    names.append(name)
print(m,f)