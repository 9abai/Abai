#[{"к":"начение","к":"начение","к":"начение"},
# {"к":"начение","к":"начение","к":"начение"},
# {"к":"начение","к":"начение","к":"начение"}]
spisok = []

def printer():
    slovar = {}
    b = input("Введите марку авто: ")
    m = input("Введите модель данного авто: ")
    y = input("Введите год данного авто: ")
    slovar['brand']= b
    slovar['model']= m
    slovar['year']= y
    spisok.append(slovar)

while len(spisok) < 3:
    printer()
print(spisok)