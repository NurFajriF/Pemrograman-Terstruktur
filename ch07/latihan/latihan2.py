
pilihfile = input('Masukkan nama file: ')
try:
    file = open(pilihfile , "r")
    print(file.read())
except FileNotFoundError:
    print('File tidak ditemukan')
try:
    file = open(pilihfile, "a")
    while True:
        data_tambahan = input('Data yang mau ditambahkan: ')
        file.writelines(data_tambahan)
        ubahlagi = "y"
        ubahlagi = input('Mau lagi (y/n): ')
        if(ubahlagi == "n"):
            break
            file.close()
except PermissionError:
    print('File tidak ditemukan')
