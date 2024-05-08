def inisial(daftar):
    nama = dict()
    for i in daftar:
        if i[0] in nama.keys():
            nama[i[0]] += 1
            print(f"{i}{nama[i[0]]}")
        else:
            nama[i[0]] = 1
            print(i)

daftar= ("Michael","Miny","Miboli","Mautin")
inisial(daftar)
