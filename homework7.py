x = int(input("Введите первое значене(целое число): "))
y = int(input("Введите второе значение(целое число): "))
z = float(input("Введите не целое число: "))

from mymath import other
other.round(z)
print(other.round(z))

import mymath.operations.arithmetic as m
m.add(x,y)
print(m.add(x,y))

import mymath.operations.trigonometric as trig
trig.sin(x,z)
print(trig.sin(x,z))