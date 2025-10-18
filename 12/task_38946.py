# https://inf-ege.sdamgia.ru/problem?id=38946


st = '1' * 201
for i in range(201, 301):
    st = '1' * i
    while ('111' in st) or ('222' in st):
        st = st.replace('111', '22', 1)
        st = st.replace('222', '1', 1)
    if not '2' in st:
        print(i)
        break