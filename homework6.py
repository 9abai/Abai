# написать программу, которая запрашивает и сохраняет данные о пользователе в файл +
# для каждого пользователя заводится отдельный файл, предварительно проверив, есть ли уже с таким именем
# у программы три режима работы - вывод всех файлов с пользователями; выбор файла и вывод данных;
# создание новой записи, путем введения новых данных;

import json, os
l = {}

def questions():
    n = input("Введите ваше имя: ")
    ln = input("Введите вашу фамилию: ")
    y = str(input("Введите год вашего рождения: "))
    l['name'] = n
    l['last name'] = ln
    l["year"] = y

jfile = 'lesson6_data/users/'

print("Здравствуйте пользователь! \nЭто программа прдназначена для ввода ваших данных и предварительно сохранив их!")
def questions2():
    o = int(input("Какую операцию мы будем проводить?\n"
              "1) Создать данные\n"
              "2) Просматреть список данных\n"
              "3) Изменить существующие данные\n"
              "4) Завершить работу\n"
              "Выберите номер функции: "))
    return o

def play():
    o= questions2()
    directory = os.listdir("lesson6_data/users")
    if o == 1:
        #for index in enumerate(jfile):
        questions()
        with open (jfile + l['name'] + l['last name'] + ".json",'w') as f:
            json_str = json.dumps(l)
            f.write(json_str)
            print(json_str)


    elif o == 2:
        for index, file in enumerate(directory):
            print(index, ':', file)

    elif o == 3:
        for index, file in enumerate(directory):
            print(index, ':', file)
        n = input("Впешите номер файла, данные которого вы хотите изменить: ")
        with open(jfile+directory[int(n)], 'w') as f:
            questions()
            json_str = json.dumps(l)
            f.write(json_str)

    else:
        print("Введены неверные значения! Попробуйсте ещё раз")
    if o != 4:
        play()


play()
print("Работа завершена")