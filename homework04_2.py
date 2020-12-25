names = []
m = []
f = []

while len(names) < 5:
    name = input("Введите имя: ")
    g =  input("их гендер: ")
    if g == "m":
        m.append(name)
    elif g == 'f':
        f.append(name)
    names.append(name)
print(m)
print(f)