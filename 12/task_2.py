# https://inf-ege.sdamgia.ru/problem?id=10290

r = '1' + '8' * 80
while '18' in r or '288' in r or '3888' in r:
    if '18' in r:
        r = r.replace('18','2',1)
    elif '288' in r:
        r = r.replace('288','3',1)
    else:
        r = r.replace('3888', '1',1)
print(r)