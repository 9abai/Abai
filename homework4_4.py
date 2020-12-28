vse = ['kartoshka', 'smorodina', 'yabloki', 'grushi','morkovka', 'luk', 'pomidor', 'apelsini','arbuz']
ovoshi = ['kartoshka', 'morkovka', 'luk', 'pomidor']
frukti = ['yabloki', 'grushi', 'apelsini']


for i in vse:
    if i in ovoshi:
        print(i, "это овощ")
    elif i in frukti:
        print(i, "это фрукт")
    else:
        print(i, "- это ягода")