s = input("Введите Ваше предложение: ")
i = 0
l = ''

while i < len(s):
    if i % 2 == 0:
        l = l + s[i].upper()
    else:
        l = l + s[i].lower()
    i = i + 1
print(l)