def hapus(data,angka):
    akhir = []
    for i in data:
        if type(i) == tuple:
            a = list()
            for j in i:
                if j == angka:
                    continue
                a.append(j)
            akhir.append(tuple(a))
        else:
            if i == angka:
                continue
            else:
                akhir.append(i)
    print(tuple(akhir))

data = (1, 2, 3, 4, 5, 6, 7, 8, 9)
hapus(data, 3)
